<template>
  <div class="zlda-content">
    <div class="container">
      <div class="shop-inners">
        <h4>Shop collections</h4>
        <div class="card-inners" v-for="item in goodsClassList">
          <div class="card-inner background-gray70 block-link col-sm-4 col-md-3 col-lg-3 grid-item">
            <div class="pro-class">
              <div class="inner">
                <div class="wrap">
                  <div class="image">
                    <router-link :to="{  name: 'class',  params: { userId: item.GoodsId }}">
                      <a href="detail.html" target="_blank">
                        <div class="display front">
                          <img v-bind:src="item.goodsClassListImg" alt="..." class="img-rounded img-responsive">
                          <span>{{item.goodsClassListsName}}</span>
                        </div>
                        <div class="display back">
                          <h6 style="color:#000000;">{{item.goodsClassListsName}}</h6>
                        </div>
                      </a>
                    </router-link>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container" style="margin-top: 150px">
      <div class="shop-card" v-for="item in goodsIndexShow">
        <div class="aaaa"
             style="background: linear-gradient(#ecf0f1,#ffffff);font-family: Arial,sans-serif">
          <div class="text col-md-4" style="position: absolute;margin-left: 50px">
            <h2 style="color: #444444">{{item.goodsIndexShowListName}}</h2>
            <p style="color: #848484">{{item.goodsIndexShowListIntro}}</p>
            <h4 style="color: #444;font-size: 1em">US${{item.goodsIndexShowListPrice}}起</h4>
            <a href=""><span>SHOP NOW</span></a>
          </div>
          <img class="img-responsive" v-bind:src="item.goodsIndexShowListImg" alt="">
        </div>
      </div>
      <!--<div class="shop-card">-->
      <!--<div class="aaaa" style="background: linear-gradient(#ecf0f1,#ffffff)">-->
      <!--<img class="img-responsive" src="img/GoogleWifi.webp" alt="">-->
      <!--</div>-->
      <!--</div>-->
      <!--<div class="shop-card">-->
      <!--<div class="aaaa" style="background: linear-gradient(#ecf0f1,#ffffff)">-->
      <!--<img class="img-responsive" src="img/Daydream.webp" alt="">-->
      <!--</div>-->
      <!--</div>-->
      <!--<div class="shop-card">-->
      <!--<div class="aaaa" style="background: linear-gradient(#ecf0f1,#ffffff)">-->
      <!--<img class="img-responsive" src="img/Chromecast.webp" alt="">-->
      <!--</div>-->
      <!--</div>-->
    </div>
  </div>
</template>
<script>
  import axios from 'axios'
  export default {
    data () {
      return {
        goodsClassList: [],
        goodsIndexShow: []
      }
    },
    created: function () {
      axios.get('/api/goodsclass').then((response) => {
        response = response.data
        if (response.status === '200') {
          this.goodsClassList = response.goodsClassList
        }
      })
      axios.get('/api/goodsindexshow').then((response) => {
        response = response.data
        if (response.status === '200') {
          this.goodsIndexShow = response.goodsIndexShowList
        }
      })
    },
    methods: {}
  }
</script>
<style></style>
