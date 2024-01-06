<script lang="ts">
  //@ts-nocheck
  import { athletes } from "$lib/stores";
  import { Avatar } from "@skeletonlabs/skeleton";
  import { Accordion, AccordionItem } from "@skeletonlabs/skeleton";
  import { getModalStore, type ModalSettings } from "@skeletonlabs/skeleton";
  import { TabGroup, Tab, TabAnchor } from "@skeletonlabs/skeleton";

  const modalStore = getModalStore();
  let tabSet: number = 0;

  function deleteAthlete(athleteToDelete: Object): void {
    const confirmDelete: ModalSettings = {
      type: "confirm",
      title: "Delete Athlete",
      buttonTextConfirm: "DELETE PERMENANTLY",
      body:
        "Are you sure you want to remove " +
        athleteToDelete.firstName +
        "?" +
        " This cannot be undone, all athlete throw history will also be delted",
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
    <a href="athletes/new" class="btn variant-ghost-secondary">Add New</a>
  </div>
  <div class="card-body">
    <Accordion>
      {#if !$athletes.length}
        <span class="ml-4">No Athletes Yet</span>
      {/if}
      {#each $athletes as athlete}
        <AccordionItem autocollapse>
          <svelte:fragment slot="lead"
            ><Avatar
              width="w-16"
              initials={athlete.initials}
              background="bg-secondary-500/60"
            /></svelte:fragment
          >
          <svelte:fragment slot="summary"
            ><span class="text-xl">{athlete.firstName} {athlete.lastName}</span
            ></svelte:fragment
          >
          <svelte:fragment slot="content">
            <TabGroup>
              <Tab bind:group={tabSet} name="tab1" value={0}>
                <span>Throw Sessions</span>
              </Tab>
              <Tab bind:group={tabSet} name="tab2" value={1}>Info</Tab>
              <Tab bind:group={tabSet} name="tab3" value={2}>Settings</Tab>
              <Tab bind:group={tabSet} name="tab4" value={3}>Metrics</Tab>
              <!-- Tab Panels --->
              <svelte:fragment slot="panel">
                {#if tabSet === 0}
                  {#if athlete.throws.length > 0}
                    <Accordion>
                      {#each athlete.throws as session}
                        <AccordionItem>
                          <svelte:fragment slot="lead">🏈</svelte:fragment>
                          <svelte:fragment slot="summary"
                            >{session.createdAt}</svelte:fragment
                          >
                          <svelte:fragment slot="content">
                            <ul
                              class="list ml-4 w-full md:w-1/2 lg:w/12 variant-soft-surface rounded-md p-4"
                            >
                              <li>
                                <span class="flex-auto">Arm Angle</span>
                                <span>{session.armAngle}</span>
                              </li>
                              <li>
                                <span class="flex-auto">Release Time</span>
                                <span>{session.releaseTime}</span>
                              </li>
                              <li>
                                <span class="flex-auto">Release Height</span>
                                <span>{session.releaseHeight}</span>
                              </li>
                              <li>
                                <span class="flex-auto">Shoulder Tilt</span>
                                <span>{session.shoulderTilt}</span>
                              </li>
                              <br />
                              <li>
                                <button class="btn variant-soft-error text-sm"
                                  >Remove Throw Session</button
                                >
                              </li>
                            </ul>
                          </svelte:fragment>
                        </AccordionItem>
                      {/each}
                    </Accordion>
                  {:else}
                    No Throws Recorded Yet
                  {/if}
                {:else if tabSet === 1}
                  <ul
                    class="list ml-4 w-full md:w-1/2 lg:w/12 variant-soft-surface rounded-md p-4"
                  >
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
                  </ul>
                {:else if tabSet === 2}
                  <div class="flex justify-start ml-5">
                    <button
                      class="btn variant-soft-surface text-sm mr-2"
                      on:click={() => console.log("do something")}
                      >Edit Athlete</button
                    >
                    <button
                      class="btn variant-soft-error text-sm"
                      on:click={() => deleteAthlete(athlete)}
                      >Remove Athlete</button
                    >
                  </div>
                {:else if tabSet === 3}
                  <div class="flex justify-start ml-5">
                    <span class="badge variant-ghost-tertiary p-4 text-lg"
                      >Coming Soon</span
                    >
                  </div>
                {/if}
              </svelte:fragment>
            </TabGroup>
          </svelte:fragment>
        </AccordionItem>
      {/each}
    </Accordion>
  </div>
</div>
