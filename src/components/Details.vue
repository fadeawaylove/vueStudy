<template>
    <div id="details">
        <el-container style="height:100%; border: 1px solid #eee">

             <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
                <!-- 侧边栏 -->
                <!-- 导航栏 默认开启第一个 -->
                <el-menu :default-openeds="['1']"> 
                    <!-- 子选项 -->
                    <el-submenu index="1">
                        <template slot="title"><i class="el-icon-message"></i>流程信息图表</template>
                            <el-menu-item-group>
                                <!-- <template slot="title">流程实时图</template> -->
                                <el-menu-item index="1-1" @click="requestData1()">实时折线图</el-menu-item>
                                <el-menu-item index="1-2">选项2</el-menu-item>
                            </el-menu-item-group>
                            <el-menu-item-group title="分组2">
                                <el-menu-item index="1-3">选项3</el-menu-item>
                            </el-menu-item-group>
                        <el-submenu index="1-4">

                        <template slot="title">选项4</template>
                        <el-menu-item index="1-4-1">选项4-1</el-menu-item>
                        </el-submenu>
                    </el-submenu>

                    <el-submenu index="2">
        <template slot="title"><i class="el-icon-menu"></i>导航二</template>
        <el-menu-item-group>
          <template slot="title">分组一</template>
          <el-menu-item index="2-1">选项1</el-menu-item>
          <el-menu-item index="2-2">选项2</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group title="分组2">
          <el-menu-item index="2-3">选项3</el-menu-item>
        </el-menu-item-group>
        <el-submenu index="2-4">
          <template slot="title">选项4</template>
          <el-menu-item index="2-4-1">选项4-1</el-menu-item>
        </el-submenu>
      </el-submenu>

                <el-submenu index="3">
        <template slot="title"><i class="el-icon-setting"></i>导航三</template>
        <el-menu-item-group>
          <template slot="title">分组一</template>
          <el-menu-item index="3-1">选项1</el-menu-item>
          <el-menu-item index="3-2">选项2</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group title="分组2">
          <el-menu-item index="3-3">选项3</el-menu-item>
        </el-menu-item-group>
        <el-submenu index="3-4">
          <template slot="title">选项4</template>
          <el-menu-item index="3-4-1">选项4-1</el-menu-item>
        </el-submenu>
      </el-submenu>
                </el-menu>
                
            </el-aside>

            <el-container>
                <el-main id="mainContent" >
                    <!-- 这是内容展示区域 -->
                    <!-- 这个div里面装图表之类的内容 -->
                    <div :id="currentChart" style="height: 100%" ref="chartArea"></div>


                </el-main>
            </el-container>

        </el-container>




    </div>
</template>

<script>
import constantDict from '../model/constants.js'
import router from '../router/router.js';
import storage from '../model/storage.js';

export default {
    data(){
        return {
            app_version:'',
            currentChart:'table1'

        }
    },
    mounted(){
        // 注意 这里是route而不是router
        this.app_version = storage.get("currentAppVersion");
        if(!this.app_version){
            // 如果没有app_version 就跳转回home入口
            this.$router.push("home");
        }
        // 默认请求一下折线图的信息
        this.requestData1(this.app_version);
    }
    ,
    methods :{
        requestData1(app_version){
            // 请求数据
            this.$http.post(constantDict.HOST + "details", {app_version:app_version}).then(
                resp => {
                    // 返回数据是否成功
                    if(resp.body.success == "true"){
                        // 组装数据
                        function addData(shift) {
                                now = [now.getFullYear(), now.getMonth() + 1, now.getDate()].join('/');
                                date.push(now);
                                data.push((Math.random() - 0.4) * 10 + data[data.length - 1]);

                                if (shift) {
                                    date.shift();
                                    data.shift();
                                }


                        // 渲染图表
                        option = {
                                xAxis: {
                                    type: 'category',
                                    boundaryGap: false,
                                    data: date
                                },
                                yAxis: {
                                    boundaryGap: [0, '50%'],
                                    type: 'value'
                                },
                                series: [
                                    {
                                        name:'成交',
                                        type:'line',
                                        smooth:true,
                                        symbol: 'none',
                                        stack: 'a',
                                        areaStyle: {
                                            normal: {}
                                        },
                                        data: data
                                    }
                                ]
                            };
                            setInterval(function () {
                                        addData(true);
                                        myChart.setOption({
                                            xAxis: {
                                                data: date
                                            },
                                            series: [{
                                                name:'成交',
                                                data: data
                                            }]
                                        });
                                    }, 500);



                    }else{
                        alert(resp.body.errmsg)
                    }

                },
                err => {
                    this.$router.push("login");
                }
            )

        }
    }
}
</script>



<style lang="scss" scoped>
  .el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 60px;
  }
  
  .el-aside {
    color: #333;
  }
</style>
