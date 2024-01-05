<script lang="ts">
  //@ts-nocheck
  import { historyStore } from "$lib/stores";
  import { Accordion, AccordionItem } from "@skeletonlabs/skeleton";
  import { getModalStore } from "@skeletonlabs/skeleton";

  const modalStore = getModalStore();

  function deleteThrow(throwId: string): void {
    const confirmDelete: ModalSettings = {
      type: "confirm",
      title: "Delete Throw",
      body: "Are you sure you want to delete this record?",
      response: (r: boolean) => {
        if (r) {
          historyStore.update((throws) =>
            throws.filter((n) => n.id !== throwId),
          );
          return;
        }
      },
    };

    modalStore.trigger(confirmDelete);
  }
</script>

<div class="card p-4 h-auto h-auto">
  <div class="card-header mb-10 flex justify-between align-baseline">
    <p class="text-xl">Your Throw History</p>
  </div>
  <div class="card-body">
    {#if $historyStore.length > 0}
      <Accordion>
        {#each $historyStore as throwSession}
          <AccordionItem open={false}>
            <svelte:fragment slot="lead">🏈</svelte:fragment>
            <svelte:fragment slot="summary"
              ><div class="flex justify-start">
                <span class="font-bold text-xl mr-auto"
                  >{throwSession.qbName === undefined
                    ? "No Name QB"
                    : throwSession.qbName}</span
                >
                <span class="badge text-sm variant-soft-surface"
                  >{throwSession.createdAt}</span
                >
              </div>
            </svelte:fragment>
            <svelte:fragment slot="content">
              <ul class="list ml-10 w-1/2 variant-soft-surface rounded-md p-4">
                <li>
                  <span class="flex-auto">Arm Angle</span>
                  <span>{throwSession.armAngle}</span>
                </li>
                <li>
                  <span class="flex-auto">Release Time</span>
                  <span>{throwSession.releaseTime}</span>
                </li>
                <li>
                  <span class="flex-auto">Release Height</span>
                  <span>{throwSession.releaseHeight}</span>
                </li>
                <li>
                  <span class="flex-auto">QB Height</span>
                  <span>{throwSession.qbHeight}</span>
                </li>
                <li>
                  <span class="flex-auto">Shoulder Tilt</span>
                  <span>{throwSession.shoulderTilt}</span>
                </li>
                <br />
                <li>
                  <button
                    class="btn variant-soft-error text-sm"
                    on:click={() => deleteThrow(throwSession.id)}
                    >Remove Throw Session</button
                  >
                </li>
              </ul>
            </svelte:fragment>
          </AccordionItem>
        {/each}
      </Accordion>
    {:else}
      <p class="badge p-4 variant-soft-secondary">
        You do not have any saved throws yet
      </p>
    {/if}
  </div>
</div>
