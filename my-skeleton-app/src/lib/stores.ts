import { localStorageStore } from "@skeletonlabs/skeleton";

import type { Writable } from "svelte/store";

type Throw = {
    id: string,
    armAngle: string
    shoudlerTilt: string
    releaseTime: string
    releaseHeight: string
    qbHeight: string
    qbName: string
    createdAt: string
}

export const historyStore: Writable<Throw[]> = localStorageStore('history', [])