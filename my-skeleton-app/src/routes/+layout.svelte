<script lang="ts">
  //@ts-nocheck

  import Navigation from "$lib/components/Navigation.svelte";
  import "../app.postcss";
  import {
    AppShell,
    AppBar,
    Avatar,
    initializeStores,
    getDrawerStore,
    Drawer,
    Toast,
    getToastStore,
    Modal,
    LightSwitch,
  } from "@skeletonlabs/skeleton";

  initializeStores();

  const drawerStore = getDrawerStore();

  function drawerOpen(): void {
    drawerStore.open();
  }
</script>

<Toast position="tr"></Toast>
<Modal></Modal>
<Drawer>
  <Navigation />
</Drawer>

<!-- App Shell -->

<AppShell slotSidebarLeft="w-0 md:w-52 bg-surface-500/10">
  <svelte:fragment slot="header">
    <!-- App Bar -->
    <AppBar>
      <svelte:fragment slot="lead">
        <!-- <button class="md:hidden btn btn-sm mr-4" on:click={drawerOpen}>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="icon icon-tabler icon-tabler-menu"
						width="24"
						height="24"
						viewBox="0 0 24 24"
						stroke-width="2"
						stroke="currentColor"
						fill="none"
						stroke-linecap="round"
						stroke-linejoin="round"
						><path
							stroke="none"
							d="M0 0h24v24H0z"
							fill="none"
						/><path d="M4 8l16 0" /><path d="M4 16l16 0" /></svg
					>
				</button> -->

        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="icon icon-tabler icon-tabler-eye-bolt"
          width="24"
          height="24"
          viewBox="0 0 24 24"
          stroke-width="2"
          stroke="currentColor"
          fill="none"
          stroke-linecap="round"
          stroke-linejoin="round"
          ><path stroke="none" d="M0 0h24v24H0z" fill="none" /><path
            d="M10 12a2 2 0 1 0 4 0a2 2 0 0 0 -4 0"
          /><path
            d="M13.1 17.936a9.28 9.28 0 0 1 -1.1 .064c-3.6 0 -6.6 -2 -9 -6c2.4 -4 5.4 -6 9 -6c3.6 0 6.6 2 9 6"
          /><path d="M19 16l-2 3h4l-2 3" /></svg
        >

        <strong class="text-xl uppercase ml-2"> <a href="/">Optic</a></strong>
        <span class="text-sm ml-3 variant-soft"> a sports vision company</span>
      </svelte:fragment>

      <svelte:fragment slot="trail">
        <a
          class="btn variant-filled-secondary hover:variant-soft-secondary"
          href="/analyzer">Throw Analyzer</a
        >
        <a
          class="btn variant-outline-secondary hover:variant-soft-secondary"
          href="/athletes">Athletes</a
        >
        <a
          class="btn variant-outline-secondary hover:variant-soft-secondary"
          href="/history">Throw History</a
        >
        <LightSwitch />
      </svelte:fragment>
    </AppBar>
  </svelte:fragment>

  <!-- <svelte:fragment slot="sidebarLeft">
		<Navigation />
	</svelte:fragment> -->

  <div class="container p-10 mx-auto">
    <slot />
  </div>

  <svelte:fragment slot="pageFooter"
    ><div class="p-4 text-primary-100">
      A Colby Sprague Project
    </div></svelte:fragment
  >
</AppShell>
