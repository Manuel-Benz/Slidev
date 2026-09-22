import { defineKatexSetup } from '@slidev/types'

export default defineKatexSetup(() => {
	return {
		macros: {
			'\\P': '\\operatorname{P}',
		},
	}
})
