<template>
    <div>
        <div class="recommend-title">热销推荐</div>
        <ul>
            <router-link class="item" v-for="item of list" :key=item.id>
                <img :src="item.imgUrl" class="item-img" />
                <div class="item-info">
                    <p class="item-title">{{item.title}}</p>
                    <p class="item-desc">{{item.desc}}</p>
                    <button class="item-button">查看详情</button>
                </div>
            </router-link>
        </ul>
    </div>
</template>

<script>
/* eslint-disable*/
export default {
  name: "List_1",
  data () {
    return {
        list: [
            {
                id: "0001",
                imgUrl: "//dimg07.c-ctrip.com/images/100e0h0000008rp39A12F_C_221_166.jpg",
                title: "故宫",
                desc: "东方宫殿建筑代表，世界宫殿建筑典范"
            },
            {
                id: "0002",
                imgUrl: "//dimg07.c-ctrip.com/images/100e0h0000008rp39A12F_C_221_166.jpg",
                title: "故宫",
                desc: "东方宫殿建筑代表，世界宫殿建筑典范"
            },
            {
                id: "0003",
                imgUrl: "//dimg07.c-ctrip.com/images/100e0h0000008rp39A12F_C_221_166.jpg",
                title: "故宫",
                desc: "东方宫殿建筑代表，世界宫殿建筑典范"
            },
            {
                id: "0004",
                imgUrl: "//dimg07.c-ctrip.com/images/100e0h0000008rp39A12F_C_221_166.jpg",
                title: "故宫",
                desc: "东方宫殿建筑代表，世界宫殿建筑典范"
            },
            {
                id: "0005",
                imgUrl: "//dimg07.c-ctrip.com/images/100e0h0000008rp39A12F_C_221_166.jpg",
                title: "故宫",
                desc: "东方宫殿建筑代表，世界宫殿建筑典范"
            },
            {
                id: "0006",
                imgUrl: "//dimg07.c-ctrip.com/images/100e0h0000008rp39A12F_C_221_166.jpg",
                title: "故宫",
                desc: "东方宫殿建筑代表，世界宫殿建筑典范"
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
    line-height: px2rem(50);
    height: px2rem(50);
    background: #eee;
    text-indent: px2rem(30);
    font-size: px2rem(30);
    font-weight: 500;
}
.item{
    overflow: hidden;
    display: flex;
    height: px2rem(200);
    border-bottom: solid #eee 1px;
    .item-img{
        height: 80%;
        margin-top: px2rem(2)
    }
    // .item-info{
    //     height: 80%;
    //     flex: 1;
    //     padding: px2rem(8);
    //     margin-top: px2rem(4);
    //     min-width: 0;
    //     .item-title{
    //         line-height: px2rem(30);
    //         height: px2rem(30);
    //         font-size: px2rem(30);
    //         @include ellipsis();
    //         margin: px2rem(8) px2rem(8);
    //     }
    //     .item-desc{
    //         line-height: px2rem(25);
    //         height: px2rem(25);
    //         @include ellipsis();
    //         color: #ccc;
    //         font-size: px2rem(25);
    //         margin: px2rem(2);
    //     }
    //     .item-button{
    //         height: px2rem(30);
    //         line-height: px2rem(30);
    //         width: px2rem(150);
    //         background: #ff9300;
    //         margin: px2rem(16);
    //         border-radius: px2rem(2);
    //         border: 1px;
    //         color: #fff;
    //         font-size: px2rem(25);
    //     }
    // }
    .item-info{
        height: 80%;
        flex: 1;
        padding: px2rem(8);
        margin-top: px2rem(4);
        min-width: 0;
        .item-title{
            // line-height: 40%;
            height: 40%;
            font-size: px2rem(30);
            @include ellipsis();
            margin: px2rem(8) px2rem(8);
        }
        .item-desc{
            // line-height: 40%;
            height: 40%;
            @include ellipsis();
            color: #ccc;
            font-size: px2rem(25);
            margin: px2rem(2);
        }
        .item-button{
            height: 20%;
            // line-height: 20%;
            width: px2rem(150);
            background: #ff9300;
            // margin: px2rem(16);
            border-radius: px2rem(2);
            border: 1px;
            color: #fff;
            font-size: px2rem(25);
        }
    }
}
</style>