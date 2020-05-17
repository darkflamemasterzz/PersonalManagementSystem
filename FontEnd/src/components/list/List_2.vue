<template>
    <div>
        <div class="recommend-title">周末去哪</div>
        <ul>
            <li class="item" v-for="item of list" :key="item.id">
                <div class="item-img-wrapper">
                    <img class="item-img" :src='item.imgUrl' />
                </div>
                <div class="item-info">
                    <p class="item-title">{{item.title}}</p>
                    <p class="item-desc">{{item.desc}}</p>
                </div>
            </li>
        </ul>
    </div>
</template>

<script>
/* eslint-disable*/
export default {
  name: "List_2",
  data () {
    return {
        list: [
            {
                id: "0001",
                imgUrl: "https://dimg04.c-ctrip.com/images/3507180000014tiu9EF0E_C_280_158.jpg",
                title: "北京温泉排行榜",
                desc: "细数北京温泉，温暖你的冬天"
            },
            {
                id: "0002",
                imgUrl: "https://dimg04.c-ctrip.com/images/3507180000014tiu9EF0E_C_280_158.jpg",
                title: "北京温泉排行榜",
                desc: "细数北京温泉，温暖你的冬天"
            },
            {
                id: "0003",
                imgUrl: "https://dimg04.c-ctrip.com/images/3507180000014tiu9EF0E_C_280_158.jpg",
                title: "北京温泉排行榜",
                desc: "细数北京温泉，温暖你的冬天"
            }
        ]
    }
  }
}
</script>

<style lang="scss" scoped>
@import '../../assets/styles/global.scss';

.recommend-title{
    margin-top: px2rem(16);
    height: px2rem(50);
    line-height: px2rem(50);
    background: #eee;
    text-indent: px2rem(30);
    font-size: px2rem(30);
    font-weight: 500;
}
.item{
    overflow: hidden;
    border-bottom: solid #eee 1px;
    margin-bottom: px2rem(10);
    .item-img-wrapper{
        overflow: hidden;
        height: 0;
        padding-bottom: 33.9%;
        .item-img{
            width: 100%;
        }
    }
    .item-info{
        padding: px2rem(8);
        .item-title{
            line-height: px2rem(30);
            font-size: px2rem(30);
            @include ellipsis()
        }
        .item-desc{
            line-height: px2rem(25);
            color: #ccc;
            font-size: px2rem(25);
        }
    }
}
</style>