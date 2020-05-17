<template>
    <div class="icons">
        <swiper :options="swiperOptions">
            <swiper-slide v-for="(page, index) of pages" :key="index">
                <div class="icon" v-for="item of page" :key="item.id">
                    <div class="icon-img">
                        <img :src="item.imgUrl" class="icon-img-content">
                    </div>
                    <p class="icon-desc">{{item.desc}}</p>
                </div>
            </swiper-slide>
            <div class="swiper-pagination" slot="pagination"></div>
        </swiper>
    </div>
</template>

<script>
/* eslint-disable*/
export default {
  name: "IconList",
  data () {
    return {
        swiperOptions: {
            pagination: {
                pagination: {
                    el: '.swiper-pagination',
                    loop: true
                },
            },
        },

        iconList: [
            {
                id: "0001",
                imgUrl: "http://s.qunarzz.com/homenode/images/touchheader/hotel.png",
                desc: "酒店"
            },
            {
                id: "0002",
                imgUrl: "//s.qunarzz.com/homenode/images/touchheader/flight.png",
                desc: "机票"
            },
            {
                id: "0003",
                imgUrl: "//s.qunarzz.com/homenode/images/touchheader/train.png",
                desc: "火车票"
            },
            {
                id: "0004",
                imgUrl: "//s.qunarzz.com/homenode/images/touchheader/package.png",
                desc: "度假"
            },
            {
                id: "0005",
                imgUrl: "//s.qunarzz.com/homenode/images/touchheader/piao.png",
                desc: "景点门票"
            },
            {
                id: "0006",
                imgUrl: "http://s.qunarzz.com/homenode/images/touchheader/hotel.png",
                desc: "酒店"
            },
            {
                id: "0007",
                imgUrl: "//s.qunarzz.com/homenode/images/touchheader/flight.png",
                desc: "机票"
            },
            {
                id: "0008",
                imgUrl: "//s.qunarzz.com/homenode/images/touchheader/train.png",
                desc: "火车票"
            },
            {
                id: "0009",
                imgUrl: "//s.qunarzz.com/homenode/images/touchheader/package.png",
                desc: "度假"
            }
        ]
    }
  },

  computed: {
            pages () {
                const pages = []
                this.iconList.forEach((item, index) => {
                    const page = Math.floor(index/8)
                    if (!pages[page]){
                        pages[page] = []
                    }
                    pages[page].push(item)
                })

                return pages
            }
    }
}
</script>

<style lang="scss" scoped>
@import '../../assets/styles/global.scss';

.icons{
    overflow: hidden;
    margin-top: px2rem(8);

    .icon{
        position: relative;
        overflow: hidden;
        float: left;
        width: 25%;
        height: px2rem(30);
        padding-bottom: 25%;

        .icon-img{
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: px2rem(16);
            box-sizing: border-border-box;
            padding: px2rem(2);

            .icon-img-content{
                display: block;
                margin: 0 auto;
                height: 80%;
            }
        }

        .icon-desc{
            position: absolute;
            left: 0;
            right: 0;
            bottom: 0;
            height: px2rem(30);
            line-height: px2rem(30);
            text-align: center;
            color: $darkTextColor;
            font-size: px2rem(30);
            @include ellipsis();
        }
    }
}
</style>