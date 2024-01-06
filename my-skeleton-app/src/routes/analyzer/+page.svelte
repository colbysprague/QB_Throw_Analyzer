<script lang="ts">
  //@ts-nocheck
  import { Avatar, FileDropzone } from "@skeletonlabs/skeleton";
  import { ProgressBar } from "@skeletonlabs/skeleton";
  import { Stepper, Step } from "@skeletonlabs/skeleton";
  import { historyStore } from "$lib/stores";
  import { athletes } from "$lib/stores";
  import { Autocomplete } from "@skeletonlabs/skeleton";
  import Tutorial from "$lib/components/Tutorial.svelte";

  let files: FileList;
  let loading: boolean = false;
  let displayButton: boolean = true;
  let processedData;
  let videoURL;

  let athleteHeight;
  $: athleteHeight = currentAthlete
    ? parseInt(
        heightToCm(
          parseInt(currentAthlete.heightFeet),
          parseInt(currentAthlete.heightInches),
        ),
      )
    : null;

  function createThrowRecord(currentAthlete: Object): void {
    console.log(
      "Updating record for Athlete: ",
      currentAthlete.firstName,
      currentAthlete.lastName,
    );

    const throwRecord = {
      id: crypto.randomUUID(),
      armAngle: processedData.data.releaseArmAngle.toString() + " °",
      releaseHeight: processedData.data.releaseHeight.toString() + " cm",
      shoulderTilt: processedData.data.shoulderTilt.toString() + " °",
      releaseTime: processedData.data.releaseTime.toString() + " s",
      createdAt: new Date().toLocaleString(),
    };

    const athleteIdToUpdate = currentAthlete.id;

    athletes.update((allAthletes) =>
      allAthletes.map((athlete) =>
        athlete.id === athleteIdToUpdate
          ? { ...athlete, throws: [...athlete.throws, throwRecord] }
          : athlete,
      ),
    );
  }

  async function onChangeHandler(event) {
    loading = true;
    displayButton = false;

    const file = event.target.files[0];

    videoURL = URL.createObjectURL(file);

    const formData = new FormData();
    formData.append("video", file);
    formData.append("height", athleteHeight);

    try {
      const response = await fetch("http://127.0.0.1:4000/process-video", {
        method: "POST",
        mode: "cors",
        body: formData,
      });

      if (!response.ok) {
        throw new Error("Failed to process video");
      }

      const data = await response.json();
      console.log(data);

      // Assign the processed data to a variable if needed
      processedData = data[0];
      createThrowRecord(currentAthlete);
    } catch (error) {
      console.error(error);
      alert("Error Processing Video. Please try again");
    } finally {
      loading = false;
      displayButton = true;
    }
  }

  function heightToCm(feet, inches) {
    const cm = feet * 30.48 + inches * 2.54;
    return cm;
  }

  let inputDemo = "";
  let currentAthlete = null;

  const flavorOptions: AutocompleteOption<Athlete>[] = $athletes.map(
    (athlete) => ({
      label: `${athlete.firstName} ${athlete.lastName}`,
      value: athlete,
      keywords: `${athlete.firstName.toLowerCase()}, ${athlete.lastName.toLowerCase()}`,
      meta: { healthy: true }, // Adjust as needed
    }),
  );

  function onFlavorSelection(
    event: CustomEvent<AutocompleteOption<string>>,
  ): void {
    currentAthlete = event.detail.value;
  }
</script>

{#if !videoURL}
  <Tutorial />

  <div class="card my-10 p-4">
    <Stepper
      buttonComplete="variant-fighost-secondary text-xl"
      buttonCompleteLabel="Analyze"
    >
      <Step locked={false}>
        <svelte:fragment slot="header">Choose an Athlete</svelte:fragment>

        Who will be throwing the football in the clip?

        <br />

        {#if currentAthlete === null}
          <div class="text-token w-full max-w-sm space-y-2">
            <input
              class="input"
              type="search"
              name="ac-demo"
              bind:value={inputDemo}
              placeholder="Search..."
            />
            <div
              class="card w-full max-w-sm max-h-48 p-4 overflow-y-auto"
              tabindex="-1"
            >
              <Autocomplete
                bind:input={inputDemo}
                options={flavorOptions}
                on:selection={onFlavorSelection}
              />
            </div>
          </div>
        {:else}
          <div class="w-96 p-4 variant-ghost-surface rounded-full">
            <div class="flex items-center space-x-2 justify-start">
              <Avatar
                width="w-10"
                initials={currentAthlete.initials}
                background="bg-secondary-500/60"
              />
              <span class="text-xl"
                >{currentAthlete.firstName} {currentAthlete.lastName}</span
              >
            </div>
          </div>
          <button
            class="btn variant-ghost-error rounded-full text-sm"
            on:click={() => (currentAthlete = null)}>Someone Else</button
          >
        {/if}
      </Step>
      <Step>
        <svelte:fragment slot="header">Upload a Throw</svelte:fragment>
        Upload a video of you throwing the ball where your entire body is visible.
        {#if displayButton}
          <div class="p-4">
            <FileDropzone name="files" bind:files on:change={onChangeHandler}>
              <svelte:fragment slot="message">Upload a file</svelte:fragment>
            </FileDropzone>
          </div>
        {/if}
      </Step>
    </Stepper>
  </div>
{/if}

{#if videoURL}
  <div class="card card-header p-4 mb-10 flex justify-between align-baseline">
    <p class="text-xl">Your Throw Results</p>
    <button
      class="btn variant-ghost-secondary text-xl"
      on:click={() => location.reload()}
      disabled={!processedData}
      >🏈 Analyze Another Throw
    </button>
  </div>

  <div class="card">
    <div
      class="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-1 lg:grid-cols-2 rounded-sm"
    >
      <video
        class="w-full rounded-sm order-2 max-h-[calc(100vh-300px)]"
        autoplay
        muted
        loop
        playsinline
      >
        <source src={videoURL} type="video/webm" />
        <track kind="captions" srcLang="en" label="English" />
      </video>
      {#if loading}
        <section class="card w-full order-1">
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
              <span class="badge-icon p-4 variant-ghost-secondary text-xl"
                >💪</span
              >
              <span class="flex-auto">
                <dt class="font-bold text-lg mb-1 flex align-center">
                  Throwing Arm Angle
                </dt>
                <dd class="text-sm opacity-50">
                  Elbow angle upon release of the ball
                </dd>
              </span>
              <span class="text-xl">{processedData.data.releaseArmAngle}°</span>
            </div>
            <div>
              <span class="badge-icon p-4 variant-ghost-secondary text-xl"
                >🏈</span
              >
              <span class="flex-auto">
                <dt class="font-bold text-lg mb-1 flex align-center">
                  Shoudler Tilt
                </dt>
                <dd class="text-sm opacity-50">
                  Measure of shoulders parallel to ground upon release
                </dd>
              </span>
              <span class="text-xl">{processedData.data.shoulderTilt}°</span>
            </div>
            <div>
              <span class="badge-icon p-4 variant-ghost-secondary text-xl"
                >⏳</span
              >
              <span class="flex-auto">
                <dt class="font-bold text-lg mb-1 flex align-center">
                  Release Time
                </dt>
                <dd class="text-sm opacity-50">
                  Total time elapsed during throwing motion until release
                </dd>
              </span>
              <span class="text-xl"
                >{processedData.data.releaseTime}<span class="text-sm">
                  s</span
                ></span
              >
            </div>
            <div>
              <span class="badge-icon p-4 variant-ghost-secondary text-xl"
                >🪜</span
              >
              <span class="flex-auto">
                <dt class="font-bold text-lg mb-1 flex align-center">
                  Release Height <span
                    class="badge variant-soft-tertiary text-xs ml-1"
                    >Experimental</span
                  >
                </dt>
                <dd class="text-sm opacity-50">
                  Height when football is released
                </dd>
              </span>
              <span class="text-xl">
                {processedData.data.releaseHeight}<span class="text-sm">
                  cm
                </span>
              </span>
            </div>
          </dl>
        </div>
      {/if}
    </div>
  </div>
{/if}
