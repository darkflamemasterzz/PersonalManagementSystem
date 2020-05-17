<template>
  <div class="header">
      <div class="header-left iconfont">left</div>
      <div class="header-input">搜索内容</div>
      <div class="header-right">
        广州
        <!-- <span class="iconfont">&#xe606;</span> -->
      </div>
  </div>
</template>

<script>
/* eslint-disable*/
export default {
  name: "Header",
  data () {
    return {
    }
  }
}
</script>

<style lang="scss" scoped>
@import '../../assets/styles/global.scss';
.header{
  display: flex;
  height: $headerHeight;
  line-height: $headerHeight;
  background: skyblue;
  color: #fff;
  font-size: px2rem(30);
  .header-left{
        padding-left: px2rem(10);
        width: px2rem(50);
        margin: 0 0.5rem 0 0.2rem;
    }

    .header-input{
        flex: 1;
        height: px2rem(60);
        line-height: px2rem(60);
        padding-left: px2rem(20);
        margin-top: 0.6rem;
        margin-left: .01rem;
        font-size: px2rem(30);
        background: #fff;
        border-radius: .1rem;
        color: #ccc;
    }

    .header-right{
        width: px2rem(100);
        text-align: center;
        color: white;
        font-size: px2rem(30);
        .iconfont{
          font-size: 0.8rem;
    }
  }
  
}
</style>