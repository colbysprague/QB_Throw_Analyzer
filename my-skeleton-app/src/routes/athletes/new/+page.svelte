<script lang="ts">
  //@ts-nocheck
  import { athletes } from "$lib/stores";
  import { getModalStore, type ModalSettings } from "@skeletonlabs/skeleton";
  import { goto } from "$app/navigation";

  const modalStore = getModalStore();

  function addAthlete() {
    athletes.update((athlete) => [
      {
        id: crypto.randomUUID(),
        firstName: firstName,
        lastName: lastName,
        initials:
          firstName.charAt(0).toUpperCase() + lastName.charAt(0).toUpperCase(),
        number: number,
        heightFeet: feet.toString(),
        heightInches: inches.toString(),
        throws: [],
        createdAt: new Date().toLocaleString(),
      },
      ...athlete,
    ]);

    const modal: ModalSettings = {
      type: "confirm",
      // Data
      title: "New Athlete Created!",
      body: `#${number} | ${firstName + " " + lastName} | ${feet}' ${inches}"`,
      buttonTextConfirm: "See All Athletes",
      buttonTextCancel: "Add Another Athlete",
      // TRUE if confirm pressed, FALSE if cancel pressed
      response: (r: boolean) => {
        if (r) {
          goto("/athletes");
        } else {
          firstName = "";
          lastName = "";
          feet = "";
          inches = "";
          number = "";
        }
      },
    };
    modalStore.trigger(modal);

    //     console.log({
    //       id: crypto.randomUUID(),
    //       firstName: firstName,
    //       lastName: lastName,
    //       initals:
    //         firstName.charAt(0).toUpperCase() + lastName.charAt(0).toUpperCase(),
    //       number: number,
    //       throws: [],
    //       createdAt: new Date().toLocaleString(),
    //       updatedAt: null,
    //     });
    //   }

    //   function createThrowRecord(): void {
    //     athletes.update((athlete) => [
    //       ...athlete,
    //       {
    //         id: crypto.randomUUID(),
    //         firstName: firstName,
    //         lastName: lastName,
    //         initals:
    //           firstName.charAt(0).toUpperCase() + lastName.charAt(0).toUpperCase(),
    //         number: number,
    //         throws: [],
    //         createdAt: new Date().toLocaleString(),
    //       },
    //     ]);

    console.log("Updated Throw History");
  }

  let feet;
  let inches;
  let firstName;
  let lastName;
  let number;

  let validHeight = false;
  let validFeet = false;
  let validInches = false;
  let validNumber = false;

  $: validFeet = feet !== undefined && feet > 3 && feet <= 9;
  $: validInches =
    inches !== undefined && (inches === 0 || (inches > 0 && inches <= 11));
  $: validHeight = validFeet && validInches;
  $: validName =
    firstName && firstName.length > 0 && lastName && lastName.length > 0;
  $: validNumber = number !== undefined && number >= 0 && number <= 100;
  $: validForm = validName && validHeight && validNumber;
</script>

<div class="card my-10 p-4 rounded-lg w-full lg:w-2/3 mx-auto">
  <div class="card-header mb-4 flex justify-between align-baseline">
    <p class="text-xl">Add a New Athlete</p>
  </div>

  <hr class="mb-3" />

  <div class="flex-auto">
    <p class="ml-2 mb-2 text-lg">Athlete Name</p>
    {#if validForm}
      <span class="badge p-4 text-md variant-ghost-success mb-4"
        >Looks Good!</span
      >
    {:else}
      <span class="badge p-4 text-md variant-ghost-warning mb-4"
        >There is some missing information</span
      >
    {/if}

    <div class="flex justfy-start w-5/6 lg:w-1/2 space-x-2">
      <input
        class="input rounded-full"
        type="text"
        bind:value={firstName}
        placeholder="First"
      />
      <input
        class="input rounded-full"
        type="text"
        bind:value={lastName}
        placeholder="Last"
      />
    </div>
  </div>

  <div class="flex-auto mt-5">
    <p class="ml-2 mb-2 text-lg">Athlete Height</p>
    <div class="flex justfy-start w-1/2 space-x-2">
      <div class="flex items-center">
        <input
          class="w-20 input text-center border border-gray-300 rounded-full mr-1"
          type="number"
          placeholder="6"
          bind:value={feet}
        />
        <div class="mr-2">ft</div>
      </div>
      <div class="flex items-center">
        <input
          class="w-20 input text-center border border-gray-300 rounded-full mr-1"
          type="number"
          placeholder="0"
          bind:value={inches}
        />
        <div class="mr-2">in</div>
      </div>
    </div>
  </div>
  <div class="flex-auto">
    <p class="ml-2 mb-2 text-lg mt-4">Athlete Number</p>
    <span></span>
    <input
      class="w-20 input text-center border border-gray-300 rounded-full mr-1"
      type="number"
      placeholder="12"
      bind:value={number}
    />
  </div>
  <hr class="mt-4" />
  <div class="flex justify-end">
    <button
      on:click={() => addAthlete()}
      disabled={!validForm}
      class="btn variant-filled-secondary mt-5">Add New Athlete</button
    >
  </div>
</div>

<!-- <div class="card my-10 p-4">
  <Stepper
    buttonComplete="variant-fighost-secondary text-xl"
    buttonCompleteLabel="Analyze"
  >
    <Step locked={!validHeight}>
      <svelte:fragment slot="header">Enter Your Height</svelte:fragment>

      🤓 Your height will be used to calibrate the model for metrics like
      releaseHeight

      <br />
      {#if !validHeight}
        <span class="badge variant-ghost-warning mt-5"
          >Please enter a valid height</span
        >
      {:else}
        <span class="badge variant-ghost-success mt-5">Looks Good!</span>
      {/if}

      <div class="p-4">
        <input
          type="text"
          placeholder="QB Name"
          class="w-auto input text-center border border-gray-300 rounded mb-3"
          bind:value={qbName}
        />
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
  </Stepper>
</div> -->
