<template>
<div class="wrapper">
    <swiper ref="mySwiper" :options="swiperOptions">
        <swiper-slide v-for="item of swiperList" :key="item.id">
            <img class="swiper-img" :src="item.imgUrl" />
        </swiper-slide>
        <div class="swiper-pagination" slot="pagination"></div>
    </swiper>
</div>
</template>

<script>
/* eslint-disable*/
export default {
  name: "Swiper",
  data () {
    return {
        swiperList:[
            {
                "id": "0001",
                "imgUrl": "https://www.jetsetter.com/uploads/sites/7/2018/04/Yq6ObbTP-1380x690.jpeg"
            },
            {
                "id": "0002",
                "imgUrl": "https://www.pcma.org/wp-content/uploads/2019/08/Travel-tips.png"
            }
        ],
        swiperOptions: {
          pagination: {
            el: '.swiper-pagination',
            loop: true
          },
        }
    }
  },
  computed: {
      swiper() {
        return this.$refs.mySwiper.$swiper
      }
    },

    mounted() {
      console.log('Current Swiper instance object', this.swiper)
    }
}
</script>

<style lang="scss" scoped>
@import '../../assets/styles/global.scss';
.wrapper{
    overflow: hidden;
    width: 100%;
    height: 0;
    padding-bottom: 31.25%;
    .swiper-img{
        width: 100%;
    }
}
</style>