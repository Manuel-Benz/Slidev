<script setup lang="ts">
// Venn diagram for two events A and B in a sample space U.
// shade: 'none' | 'A' | 'B' | 'intersection' | 'union'
// disjoint: draw A and B as non-overlapping circles
// regions: optional labels for the regions [only A, A∩B, only B, outside]
const props = withDefaults(defineProps<{
	shade?: string
	disjoint?: boolean
	regions?: string[]
	width?: number
}>(), {
	shade: 'none',
	disjoint: false,
	width: 320,
})

const uid = Math.random().toString(36).slice(2, 8)
const a = props.disjoint ? { x: 95, y: 105, r: 55 } : { x: 125, y: 105, r: 62 }
const b = props.disjoint ? { x: 225, y: 105, r: 55 } : { x: 195, y: 105, r: 62 }
</script>

<template>
	<svg :width="width" viewBox="0 0 320 210" class="venn">
		<defs>
			<clipPath :id="`clipA-${uid}`">
				<circle :cx="a.x" :cy="a.y" :r="a.r" />
			</clipPath>
		</defs>
		<rect x="10" y="10" width="300" height="190" rx="4" class="frame" />
		<template v-if="shade === 'A' || shade === 'union'">
			<circle :cx="a.x" :cy="a.y" :r="a.r" class="fill" />
		</template>
		<template v-if="shade === 'B' || shade === 'union'">
			<circle :cx="b.x" :cy="b.y" :r="b.r" class="fill" />
		</template>
		<template v-if="shade === 'intersection'">
			<circle :cx="b.x" :cy="b.y" :r="b.r" class="fill" :clip-path="`url(#clipA-${uid})`" />
		</template>
		<circle :cx="a.x" :cy="a.y" :r="a.r" class="line" />
		<circle :cx="b.x" :cy="b.y" :r="b.r" class="line" />
		<text x="22" y="34" class="lab">U</text>
		<text :x="a.x - a.r + 2" :y="a.y - a.r + 6" class="lab">A</text>
		<text :x="b.x + b.r - 14" :y="b.y - b.r + 6" class="lab">B</text>
		<template v-if="regions">
			<text :x="disjoint ? a.x : a.x - 25" :y="a.y + 7" class="reg">{{ regions[0] }}</text>
			<text v-if="!disjoint" :x="(a.x + b.x) / 2" :y="a.y + 7" class="reg">{{ regions[1] }}</text>
			<text :x="disjoint ? b.x : b.x + 25" :y="b.y + 7" class="reg">{{ regions[2] }}</text>
			<text x="285" y="188" class="reg">{{ regions[3] }}</text>
		</template>
	</svg>
</template>

<style scoped>
.venn { display: inline-block; }
.frame { fill: none; stroke: currentColor; stroke-width: 1.5; }
.line { fill: none; stroke: currentColor; stroke-width: 2; }
.fill { fill: #bae6fd; }
.lab { font-style: italic; font-size: 20px; fill: currentColor; font-family: 'Times New Roman', serif; }
.reg { font-size: 18px; fill: currentColor; text-anchor: middle; }
</style>
