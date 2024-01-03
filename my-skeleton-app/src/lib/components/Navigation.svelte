<script lang="ts">
    import { getDrawerStore } from "@skeletonlabs/skeleton";

    const drawerStore = getDrawerStore();

    function drawerClose(): void {
        drawerStore.close();
    }
</script>

<nav class="list-nav p-4">
    <ul>
        <li><a on:click={drawerClose} href="/news">Sports News</a></li>
        <li><a on:click={drawerClose} href="/analyzer">Throw Analyzer</a></li>
    </ul>
</nav>
