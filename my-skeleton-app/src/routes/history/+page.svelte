<script>
  //@ts-nocheck
  import { historyStore } from "$lib/stores";
  import { Accordion, AccordionItem } from "@skeletonlabs/skeleton";
</script>

<div class="card p-4 h-auto">
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
              ><div class="flex justify-between">
                <span class="font-bold text-xl"
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
              <ul class="list ml-10">
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
