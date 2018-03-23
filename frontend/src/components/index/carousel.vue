<template>
<el-carousel indicator-position="inside" height="650px">
  <el-carousel-item v-for="item in carouselList" :key="item">
    <div class="">
      <img class="third-slide img-responsive" v-bind:src="item.carouselListImg" :alt="item.carouselListName">
    </div>
  </el-carousel-item>
</el-carousel>
</template>
<script>
import axios from 'axios'
export default {
  data() {
    return {
      carouselList: []
    }
  },
  created: function() {
    axios.get('/api/carousel').then((response) => {
      response = response.data
      if (response.status === '200') {
        this.carouselList = response.carouselList
      }
    })
  },
  methods: {}
}
</script>
<style>

.el-carousel__item:nth-child(2n) {
  background-color: #eef1f6;
}

.el-carousel__item:nth-child(2n+1) {
  background-color: #eef1f6;
}
.carousel-inner>.item>a>img, .carousel-inner>.item>img, .img-responsive, .thumbnail a>img, .thumbnail>img{
  margin: auto;
}
</style>
