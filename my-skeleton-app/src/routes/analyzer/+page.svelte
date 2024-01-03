<script lang="ts">
    //@ts-nocheck
    import { FileDropzone } from "@skeletonlabs/skeleton";
    import { ProgressBar } from "@skeletonlabs/skeleton";
    import { Stepper, Step } from "@skeletonlabs/skeleton";

    let files: FileList;
    let loading: boolean = false;
    let displayButton: boolean = true;
    let processedData;
    let videoURL;
    let feet;
    let inches;
    let height;

    $: calculateHeight(feet, inches);

    function calculateHeight(feet, inches) {
        // Convert feet and inches to centimeters
        const heightInCm = feet * 30.48 + inches * 2.54;

        return heightInCm;
    }

    async function onChangeHandler(event) {
        loading = true;
        displayButton = false;

        const file = event.target.files[0];

        videoURL = URL.createObjectURL(file);

        const formData = new FormData();
        formData.append("video", file);

        try {
            const response = await fetch(
                "http://127.0.0.1:4000/process-video",
                {
                    method: "POST",
                    mode: "cors",
                    body: formData,
                },
            );

            if (!response.ok) {
                throw new Error("Failed to process video");
            }

            const data = await response.json();
            console.log(data);

            // Assign the processed data to a variable if needed
            processedData = data[0];
        } catch (error) {
            console.error(error);
            alert("Error Processing Video. Please try again");
        } finally {
            loading = false;
            displayButton = true;
        }
    }

    let validFeet = false;
    let validInches = false;
    let validHeight = false;

    $: validFeet = feet !== undefined && feet >= 3 && feet <= 9;
    $: validInches = inches !== undefined && inches >= 0 && inches <= 11;
    $: validHeight = validFeet && validInches;
</script>

{#if !videoURL}
    <div class="card p-4 align-center m-0">
        <dl class="list-dl">
            <div>
                <span class="badge bg-secondary-800 p-4">📂</span>
                <span class="flex-auto">
                    <dt class="text-xl">Upload a Throw</dt>
                    <dd class="variant-soft">
                        Upload a full-body .mp4 of your throwing motion for
                        analysis - do not use a slow-motion video
                    </dd>
                </span>
            </div>
            <div>
                <span class="badge bg-secondary-800 p-4">🔎</span>
                <span class="flex-auto">
                    <dt class="text-xl">Analyzer Processes Video</dt>
                    <dd class="variant-soft">
                        Our AI Powered process will extract insights from the
                        video you provide
                    </dd>
                </span>
            </div>
            <div>
                <span class="badge bg-secondary-800 p-4">💡</span>
                <span class="flex-auto">
                    <dt class="text-xl">Gain Insight</dt>
                    <dd class="variant-soft">
                        View valuable metrics regarding your biomechanics during
                        your throwing motion
                    </dd>
                </span>
            </div>
            <hr />
        </dl>
    </div>

    <div class="card my-10 p-4">
        <Stepper
            buttonComplete="variant-filled-secondary"
            buttonCompleteLabel="Analyze"
        >
            <Step locked={!validHeight}>
                <svelte:fragment slot="header"
                    >Enter Your Height</svelte:fragment
                >

                🤓 Your height will be used to calibrate the model for metrics
                like exit velocity

                <br />
                {#if !validHeight}
                    <span class="badge variant-ghost-warning mt-5"
                        >Please enter a valid height</span
                    >
                {:else}
                    <span class="badge variant-ghost-success mt-5"
                        >Looks Good!</span
                    >
                {/if}

                <div class="p-4">
                    <div class="flex items-center space-x-2">
                        <div class="flex items-center">
                            <input
                                class="w-20 input text-center border border-gray-300 rounded mr-1"
                                type="number"
                                placeholder="6"
                                bind:value={feet}
                            />
                            <div class="mr-2">ft</div>
                        </div>
                        <div class="flex items-center">
                            <input
                                class="w-20 input text-center border border-gray-300 rounded mr-1"
                                type="number"
                                placeholder="0"
                                bind:value={inches}
                            />
                            <div class="mr-2">in</div>
                        </div>
                    </div>
                </div>
            </Step>
            <Step>
                <svelte:fragment slot="header">Upload a Throw</svelte:fragment>
                Upload a video of you throwing the ball where your entire body is
                visible.
                {#if displayButton}
                    <div class="p-4">
                        <FileDropzone
                            name="files"
                            bind:files
                            on:change={onChangeHandler}
                        >
                            <svelte:fragment slot="message"
                                >Upload a file</svelte:fragment
                            >
                        </FileDropzone>
                    </div>
                {/if}
            </Step>
            <!-- ... -->
        </Stepper>
    </div>
{/if}

{#if videoURL}
    <div class="card card-header text-center text-xl p-4 mb-10">
        Your Throw Results
    </div>
    <div class="card max-h-fit">
        <div
            class="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-1 lg:grid-cols-2 rounded-sm"
        >
            <video
                class="w-full h-auto rounded-sm"
                autoplay
                muted
                loop
                playsinline
            >
                <source src={videoURL} type="video/webm" />
                <track kind="captions" srcLang="en" label="English" />
            </video>
            {#if loading}
                <section class="card w-full">
                    <ProgressBar />

                    <div class="card-header flex justify-between items-center">
                        <div class="flex justify-center items-center space-x-4">
                            <div class="placeholder-circle w-16" />
                            <div class="placeholder-circle w-14" />
                            <div class="placeholder-circle w-10" />
                        </div>
                    </div>
                    <div class="p-4 space-y-4">
                        <div class="placeholder" />
                        <div class="grid grid-cols-4 gap-4">
                            <div class="placeholder" />
                            <div class="placeholder" />
                            <div class="placeholder" />
                            <div class="placeholder" />
                        </div>
                        <div class="placeholder" />
                        <div class="placeholder" />
                    </div>
                </section>
            {:else if processedData}
                <div class="w-full text-token card p-4 space-y-4">
                    <dl class="list-dl">
                        <div>
                            <span class="badge-icon p-4 variant-soft-secondary"
                                >💪</span
                            >
                            <span class="flex-auto">
                                <dt class="font-bold">Throwing Arm Angle</dt>
                                <dd class="text-sm opacity-50">
                                    Elbow angle upon release of the ball
                                </dd>
                            </span>
                            <span class="text-xl"
                                >{processedData.data.releaseArmAngle}</span
                            >
                        </div>
                        <div>
                            <span class="badge-icon p-4 variant-soft-secondary"
                                >🏈</span
                            >
                            <span class="flex-auto">
                                <dt class="font-bold">Shoudler Tilt</dt>
                                <dd class="text-sm opacity-50">
                                    Measure of shoulders parallel to ground upon
                                    release
                                </dd>
                            </span>
                            <span class="text-xl"
                                >{processedData.data.shoulderTilt}</span
                            >
                        </div>
                        <div>
                            <span class="badge-icon p-4 variant-soft-secondary"
                                >🚀</span
                            >
                            <span class="flex-auto">
                                <dt class="font-bold">Exit Velocity</dt>
                                <dd class="text-sm opacity-50">
                                    Exit velocity of football upon release
                                </dd>
                            </span>
                            <span class="text-xl">93 m/s</span>
                        </div>
                        <div>
                            <span class="badge-icon p-4 variant-soft-secondary"
                                >🔋</span
                            >
                            <span class="flex-auto">
                                <dt class="font-bold">Hip Torque</dt>
                                <dd class="text-sm opacity-50">
                                    Total force generated by hips during throw
                                </dd>
                            </span>
                            <span class="text-xl">14 ft/lb</span>
                        </div>
                        <div>
                            <span class="badge-icon p-4 variant-soft-secondary"
                                >🪜</span
                            >
                            <span class="flex-auto">
                                <dt class="font-bold">Release Height</dt>
                                <dd class="text-sm opacity-50">
                                    Length from ground to football upon release
                                </dd>
                            </span>
                            <span class="text-xl"
                                >{processedData.data.releaseHeight}</span
                            >
                        </div>
                    </dl>
                </div>
            {/if}
        </div>
    </div>
{/if}

<!-- <div class="h-full text-center flex flex-col align-center justify-center">
    <h1 class="h1">
        <span
            class="bg-gradient-to-br from-blue-500 to-cyan-300 bg-clip-text text-transparent box-decoration-clone"
            >Elevate Your Game.</span
        >
    </h1>

    <br />
    {#if displayButton}
        <FileButton name="files" bind:files on:change={onChangeHandler}
            >Upload Throw</FileButton
        >
    {/if}
    {#if loading}
        <ProgressBar />
    {/if}
    {#if processedData}
        <br />
        <div class="grid grid-cols-1 md:grid-cols-2">
            <video
                controls
                width="640"
                height="360"
                style="border-radius: 10px"
            >
                <source src={videoURL} type="video/mp4" />
                <track captions="" />
                Your browser does not support the video tag.
            </video>

            <div class="table-container">
                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th>On Release</th>
                            <th>Degrees</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Elbow Angle</td>
                            <td>{processedData.data.releaseArmAngle}</td>
                        </tr>
                        <tr>
                            <td>Shoulder Tilt</td>
                            <td>{processedData.data.shoulderTilt}</td>
                        </tr>
                    </tbody>
                </table>
                Thank you for using QBVision!
            </div>
        </div>
    {/if}
</div> -->
