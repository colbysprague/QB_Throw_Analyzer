<script lang="ts">
  //@ts-nocheck
  import { athletes } from "$lib/stores";
  import { Avatar } from "@skeletonlabs/skeleton";
  import { Accordion, AccordionItem } from "@skeletonlabs/skeleton";
  import { getModalStore, type ModalSettings } from "@skeletonlabs/skeleton";

  const modalStore = getModalStore();

  function deleteAthlete(athleteToDelete: Object): void {
    const confirmDelete: ModalSettings = {
      type: "confirm",
      title: "Delete Athlete",
      body:
        "Are you sure you want to remove " + athleteToDelete.firstName + "?",
      response: (r: boolean) => {
        if (r) {
          athletes.update((allAthletes) =>
            allAthletes.filter((athlete) => athlete.id !== athleteToDelete.id),
          );
          console.log($athletes);
          return;
        }
      },
    };

    modalStore.trigger(confirmDelete);
  }
</script>

<div class="card p-4 h-auto h-auto">
  <div class="card-header mb-10 flex justify-between align-baseline">
    <p class="text-xl">Your Athletes</p>
  </div>
  <div class="card-body">
    <Accordion>
      {#if !$athletes.length}
        <span class="ml-4">No Athletes Yet</span>
      {/if}
      {#each $athletes as athlete}
        <AccordionItem>
          <svelte:fragment slot="lead"
            ><Avatar
              width="w-16"
              initials={athlete.initials}
              background="bg-primary-500"
            /></svelte:fragment
          >
          <svelte:fragment slot="summary"
            ><span class="text-xl">{athlete.firstName} {athlete.lastName}</span
            ></svelte:fragment
          >
          <svelte:fragment slot="content">
            <ul class="list ml-10 w-1/2 variant-soft-surface rounded-md p-4">
              <li>
                <span class="flex-auto">Height</span>
                <span>{athlete.heightFeet}' {athlete.heightInches}"</span>
              </li>
              <li>
                <span class="flex-auto">Number</span>
                <span># {athlete.number}</span>
              </li>
              <li>
                <span class="flex-auto">Throw Sessions</span>
                <span>{athlete.throws.length}</span>
              </li>
              <li>
                <a
                  href="/history"
                  class="flex-auto text-secondary-500 underline"
                  >Throw History</a
                >
              </li>
              <hr class="my-4" />
              <div class="flex justify-between">
                <button
                  class="btn variant-soft-surface text-sm"
                  on:click={() => console.log("do something")}>Edit</button
                >
                <button
                  class="btn variant-soft-error text-sm mt-5"
                  on:click={() => deleteAthlete(athlete)}>Remove</button
                >
              </div>
            </ul>
          </svelte:fragment>
        </AccordionItem>
      {/each}
    </Accordion>
  </div>
</div>
