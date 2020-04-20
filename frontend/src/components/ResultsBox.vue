<template>
    <div class="ResultsBox" v-html="text">
        <a>Results:</a>
    </div>
</template>

<script>
export default {
    name: 'ResultsBox',
    props: {
        top5: Array,
    }
}
</script>

<style lang="css" scoped>
    .ResultsBox {
        align-items: left;
        outline: 2px;
        outline-color: black;
        width: 600px;
        height: 300px;
    }
</style>
