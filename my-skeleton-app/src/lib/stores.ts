import { localStorageStore } from "@skeletonlabs/skeleton";

import type { Writable } from "svelte/store";

type Note = {
    id: string,
    content: string;
    tags: string[],
    createdAt: number
}

export const noteStore: Writable<Note[]> = localStorageStore('notes', [])