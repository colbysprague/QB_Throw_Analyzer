
import type { CustomThemeConfig } from '@skeletonlabs/tw-plugin';

export const myCustomTheme: CustomThemeConfig = {
    name: 'my-custom-theme',
    properties: {
        // =~= Theme Properties =~=
        "--theme-font-family-base": `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace`,
        "--theme-font-family-heading": `system-ui`,
        "--theme-font-color-base": "0 0 0",
        "--theme-font-color-dark": "255 255 255",
        "--theme-rounded-base": "12px",
        "--theme-rounded-container": "8px",
        "--theme-border-base": "1px",
        // =~= Theme On-X Colors =~=
        "--on-primary": "0 0 0",
        "--on-secondary": "0 0 0",
        "--on-tertiary": "255 255 255",
        "--on-success": "0 0 0",
        "--on-warning": "0 0 0",
        "--on-error": "0 0 0",
        "--on-surface": "255 255 255",
        // =~= Theme Colors  =~=
        // primary | #0d6efd 
        "--color-primary-50": "219 233 255", // #dbe9ff
        "--color-primary-100": "207 226 255", // #cfe2ff
        "--color-primary-200": "195 219 255", // #c3dbff
        "--color-primary-300": "158 197 254", // #9ec5fe
        "--color-primary-400": "86 154 254", // #569afe
        "--color-primary-500": "13 110 253", // #0d6efd
        "--color-primary-600": "12 99 228", // #0c63e4
        "--color-primary-700": "10 83 190", // #0a53be
        "--color-primary-800": "8 66 152", // #084298
        "--color-primary-900": "6 54 124", // #06367c
        // secondary | #fd7e14 
        "--color-secondary-50": "255 236 220", // #ffecdc
        "--color-secondary-100": "255 229 208", // #ffe5d0
        "--color-secondary-200": "255 223 196", // #ffdfc4
        "--color-secondary-300": "254 203 161", // #fecba1
        "--color-secondary-400": "254 165 91", // #fea55b
        "--color-secondary-500": "253 126 20", // #fd7e14
        "--color-secondary-600": "228 113 18", // #e47112
        "--color-secondary-700": "190 95 15", // #be5f0f
        "--color-secondary-800": "152 76 12", // #984c0c
        "--color-secondary-900": "124 62 10", // #7c3e0a
        // tertiary | #6610f2 
        "--color-tertiary-50": "232 219 253", // #e8dbfd
        "--color-tertiary-100": "224 207 252", // #e0cffc
        "--color-tertiary-200": "217 195 252", // #d9c3fc
        "--color-tertiary-300": "194 159 250", // #c29ffa
        "--color-tertiary-400": "148 88 246", // #9458f6
        "--color-tertiary-500": "102 16 242", // #6610f2
        "--color-tertiary-600": "92 14 218", // #5c0eda
        "--color-tertiary-700": "77 12 182", // #4d0cb6
        "--color-tertiary-800": "61 10 145", // #3d0a91
        "--color-tertiary-900": "50 8 119", // #320877
        // success | #32eb02 
        "--color-success-50": "224 252 217", // #e0fcd9
        "--color-success-100": "214 251 204", // #d6fbcc
        "--color-success-200": "204 250 192", // #ccfac0
        "--color-success-300": "173 247 154", // #adf79a
        "--color-success-400": "112 241 78", // #70f14e
        "--color-success-500": "50 235 2", // #32eb02
        "--color-success-600": "45 212 2", // #2dd402
        "--color-success-700": "38 176 2", // #26b002
        "--color-success-800": "30 141 1", // #1e8d01
        "--color-success-900": "25 115 1", // #197301
        // warning | #fd7e14 
        "--color-warning-50": "255 236 220", // #ffecdc
        "--color-warning-100": "255 229 208", // #ffe5d0
        "--color-warning-200": "255 223 196", // #ffdfc4
        "--color-warning-300": "254 203 161", // #fecba1
        "--color-warning-400": "254 165 91", // #fea55b
        "--color-warning-500": "253 126 20", // #fd7e14
        "--color-warning-600": "228 113 18", // #e47112
        "--color-warning-700": "190 95 15", // #be5f0f
        "--color-warning-800": "152 76 12", // #984c0c
        "--color-warning-900": "124 62 10", // #7c3e0a
        // error | #dc3545 
        "--color-error-50": "250 225 227", // #fae1e3
        "--color-error-100": "248 215 218", // #f8d7da
        "--color-error-200": "246 205 209", // #f6cdd1
        "--color-error-300": "241 174 181", // #f1aeb5
        "--color-error-400": "231 114 125", // #e7727d
        "--color-error-500": "220 53 69", // #dc3545
        "--color-error-600": "198 48 62", // #c6303e
        "--color-error-700": "165 40 52", // #a52834
        "--color-error-800": "132 32 41", // #842029
        "--color-error-900": "108 26 34", // #6c1a22
        // surface | #303030 
        "--color-surface-50": "224 224 224", // #e0e0e0
        "--color-surface-100": "214 214 214", // #d6d6d6
        "--color-surface-200": "203 203 203", // #cbcbcb
        "--color-surface-300": "172 172 172", // #acacac
        "--color-surface-400": "110 110 110", // #6e6e6e
        "--color-surface-500": "48 48 48", // #303030
        "--color-surface-600": "43 43 43", // #2b2b2b
        "--color-surface-700": "36 36 36", // #242424
        "--color-surface-800": "29 29 29", // #1d1d1d
        "--color-surface-900": "24 24 24", // #181818

    }
}