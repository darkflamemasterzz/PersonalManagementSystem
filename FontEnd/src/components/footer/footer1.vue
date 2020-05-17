<template>
    <mt-tabbar v-model="selected">
      <mt-tab-item id="Home">
        <img slot="icon" src="../../assets/imgs/si-glyph-abacus.svg">
        主页
      </mt-tab-item>
      <mt-tab-item id="Member">
        <img slot="icon" src="../../assets/imgs/si-glyph-adjustment-vertical.svg">
          会员
      </mt-tab-item>
      <mt-tab-item id="Shopcart">
        <img slot="icon" src="../../assets/imgs/si-glyph-air-balloon.svg">
        购物车
      </mt-tab-item>
      <mt-tab-item id="Search">
        <img slot="icon" src="../../assets/imgs/si-glyph-airplane.svg">
        搜索
      </mt-tab-item>
    </mt-tabbar>
</template>

<script>
/* eslint-disable*/
export default {
  name: "Footer1",
  data () {
    return {
        selected: ''
    }
  }
}

</script>

<style lang="scss" scoped>
@import '../../assets/styles/global.scss';
.mint-tabbar{
    position:fixed;
    bottom:0;
}
</style>