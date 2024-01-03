//	@ts-nocheck

import { join } from 'path'
import type { Config } from 'tailwindcss'
import forms from '@tailwindcss/forms';
import { skeleton } from '@skeletonlabs/tw-plugin'
import { myCustomTheme } from './my-custom-theme'

export default {
	darkMode: 'class',
	content: ['./src/**/*.{html,js,svelte,ts}', join(require.resolve('@skeletonlabs/skeleton'), '../**/*.{html,js,svelte,ts}')],
	theme: {
		extend: {},
	},


	plugins: [
		require('@tailwindcss/forms'),
		skeleton({
			themes: {
				custom: [
					myCustomTheme
				]
			}
		})
	]

} satisfies Config;