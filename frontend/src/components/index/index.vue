<template lang="html">
  <div class="">
    <navbar></navbar>
    <carousel></carousel>
    <indexGoods></indexGoods>
  </div>
</template>

<script>
import navbar from '../common/navbar.vue'
import carousel from './carousel.vue'
import indexGoods from './IndexGoods.vue'

export default {
  components: {
    'navbar': navbar,
    'carousel': carousel,
    'indexGoods': indexGoods
  },

}
</script>
<style lang="css">
</style>
