<script>
    import { onMount } from "svelte";

    async function callAPI() {
        try {
            const response = await fetch("http://127.0.0.1:4000/test", {
                method: "GET",
                mode: "cors",
            });

            if (!response.ok) {
                throw new Error("Failed to process video");
            }

            const data = await response.json();

            console.log(data);
        } catch (error) {
            console.error(error);
        }
    }
</script>

<button on:click={callAPI}>Click me</button>
