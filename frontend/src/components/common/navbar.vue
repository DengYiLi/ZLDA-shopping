<template lang="html">
  <div class="ele-navbar">
    <el-row :gutter="20" style="margin-left:0;margin-right:0">
      <el-col :span="16">
        <el-row :gutter="20">
          <el-col :span="16" :offset="6">
            <el-menu :default-active="activeIndex2" class="el-menu-demo" mode="horizontal" @select="handleSelect" router>
              <el-menu-item index="/"><h3>ZLDA</h3></el-menu-item>
              <el-menu-item index="/">首页</el-menu-item>
              <el-submenu index="3">
                <template slot="title">类别</template>
                <div  v-for="item in goodsClassList">
                  <router-link :to="{  name: 'class',  params: { userId: item.GoodsId }}" replace>
                  <el-menu-item index="3">{{  item.goodsClassListsName }}</el-menu-item>
                </router-link>
                </div>
          </el-submenu>
<router-link to="/login"><el-menu-item index="login">个人中心</el-menu-item></router-link>
<router-link to="/cart"><el-menu-item index="login">购物车</el-menu-item></router-link>
        </el-menu>
      </el-col>
    </el-row>
      </el-col>
      <el-col :span='8' style="display: none">
        <el-row class="demo-autocomplete">
            <el-col :span="12">
                <el-autocomplete class="inline-input" v-model="state1" :fetch-suggestions="querySearch" placeholder="请输入内容" @select="handleSelect"></el-autocomplete>
            </el-col>
    </el-row>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import axios from 'axios'
import store from '../../store/store'
export default {
  data() {
    return {
      goodsInitList:[],
      goodsClassList: [],
      activeIndex: '1',
      activeIndex2: '1',
      restaurants: [],
      state1: '',
      state2: '',
      search:
          [

          ]
    };
  },
  created: function() {
      this.getGoodsClassList(),
      this.getGoodsInitList()
  },
  watch: {},
  methods: {
    querySearch(queryString, cb) {
      var restaurants = this.restaurants;
      var results = queryString ? restaurants.filter(this.createFilter(queryString)) : restaurants;
      // 调用 callback 返回建议列表的数据
      cb(results);
    },
    createFilter(queryString) {
      return (restaurant) => {
        return (restaurant.value.indexOf(queryString.toLowerCase()) === 0);
      };
    },
    loadAll() {
        this.getGoodsInitList();
      return this.search
    },
    handleSelect(item) {
      console.log(item);
    },
    getGoodsClassList:function () {
          axios.get('/api/goodsclass').then((response) => {
              response = response.data
              if (response.status === '200') {
                  this.goodsClassList = response.goodsClassList
              }
          })
      },
    getGoodsInitList:function () {
          axios.get('/api/goodsInit').then((response) => {
              response = response.data
              if (response.status === '200') {
                  this.goodsInitList = response.goodsInitList
              }
          })
      }
  },
  mounted() {
    this.restaurants = this.loadAll()
  },
}
</script>

<style lang="css">
.el-input{
  margin-top: 12px;
}

</style>
