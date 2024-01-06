<script lang="ts">
    import { getDrawerStore } from "@skeletonlabs/skeleton";

    const drawerStore = getDrawerStore();

    function drawerClose(): void {
        drawerStore.close();
    }
</script>

<nav class="list-nav p-1">
    <ul>
        <li><a on:click={drawerClose} href="/athletes">🏋️ Athletes</a></li>
        <li>
            <a on:click={drawerClose} href="/analyzer">💪 Throw Analyzer</a>
        </li>
    </ul>
</nav>
