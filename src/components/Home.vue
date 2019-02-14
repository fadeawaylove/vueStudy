<template>
    <!-- 整个页面容器 -->

    <div id='home'>
            <h2 class="flowTitle">流程概览-近30天</h2>

            <el-row>
            <el-col :span="10" v-for="(o, index) in app_version_list" :key="o" :offset="index > 0 ? 1 : 1" style="margin-top:10px">
                <el-card :body-style="{ padding: '0px' }">
                <div :id="o" style="height:300px" class="chart"></div>
                <span>{{o}}</span>
                <div style="padding: 14px;">
                    <div class="bottom clearfix">
                        <time type="flex" class="time">{{currentDate}}</time>
                        <el-button type="text" class="button" @click="requestChartData(o)">刷新</el-button>&nbsp;&nbsp;
                        <el-button type="text" class="button" @click="toDetails(o)">详情</el-button>
                    </div>
                </div>
                </el-card>
            </el-col>
            </el-row>
    </div>
</template>

<script>
import store from '../vuex/store.js'
import constantDict from '../model/constants.js'
import storage from '../model/storage.js';
import {formatDate} from '../utils/dateFormat.js'
export default {
    data(){
        return {
            pageData:[],
            app_version_list: ["PH_1", "PH_2", "VN_1"],
            currentDate: formatDate(new Date(), 'yyyy-MM-dd hh:mm')
        }
    },
    mounted (){
        this.requestData();
        this.rederAllChart();
    },
    store: store,
    methods:{
        toDetails(app_version){
            // 跳转到详情页面
            // 将当前的app_version存到页面中
            storage.set("currentAppVersion", app_version);
            // this.$router.push({name: 'details', params: {app_version: app_version}});
            this.$router.push("details");
        },
        rederAllChart(){
            this.app_version_list.forEach(element => {
                this.requestChartData(element);
            });
        },
        requestData(){
            var url = constantDict.HOST + "home"          
            this.$http.get(url).then(
                response => {
                    var indexData = response.body
                    if(indexData.success=="true"){
                        // 请求成功，可以继续获取页面数据了
                        this.pageData = indexData.data

                    }else{
                        // 获取页面数据失败
                    }
                },
                err => {
                    // 认证失败了
                    storage.remove("token");
                    this.$router.push({ name: "login" });
                    }
            )
        },
        requestChartData(app_version){
            var url = constantDict.HOST + 'flow_situation'
            // 定义chart对象
            var echarts = require('echarts');
            var myChart = echarts.init(document.getElementById(app_version));
            // 显示加载中
            myChart.showLoading({text:"正在加载中..."});
            this.$http.post(url, {app_version:app_version}).then(
                response => {
                    if(response.data.success == "true"){
                        
                        var chartData = response.body.data;    
                        var status_data = [];  // 状态数据
                        var count_data = [];  // 数量数据
                        chartData.forEach(element => {
                            status_data.push(element["status"]);
                            count_data.push(element["counts"]);
                        });                        
 
                        var tempMap = {
                            1:"新申请",
                            2:"暂态",
                            4:"人工审核",
                            5:"人工审核完毕",
                            7:"授信拒绝",
                            8:"授信通过"
                        }
                        var status_data0 = []
                        status_data.forEach(element => {          
                            status_data0.push(tempMap[element]);                
                        });
                        myChart.setOption({
                        title: {
                            // text: app_version+'授信'
                        },
                        tooltip: {},
                        xAxis: {
                            // name:"授信状态",
                            data: status_data0
                        },
                        yAxis: {
                            name: "人数"
                        },
                        series: [{
                            name: '人数',
                            type: 'bar',
                            data: count_data
                            }]
                        });

                        window.addEventListener("resize",function(){
                                myChart.resize();
                            });

                        myChart.hideLoading();//取消loading
                    }
                    
                },
                err => {
                    // console.log(err);
                    storage.remove("token");
                    this.$router.push({ name: "login" });
                }
            )
        },
        paintChart(app_version){
            var echarts = require('echarts');
            // 基于准备好的dom，初始化echarts实例
            var myChart = echarts.init(document.getElementById(app_version));
 
            var tempMap = {
                1:"新申请",
                2:"暂态",
                4:"人工审核",
                5:"人工审核完毕",
                7:"授信拒绝",
                8:"授信通过"
            }
            var status_data0 = []
            this.status_data.forEach(element => {          
                status_data0.push(tempMap[element]);                
            });
            // 绘制图表
            myChart.setOption({
                title: {
                    // text: app_version+'授信'
                },
                tooltip: {},
                xAxis: {
                    // name:"授信状态",
                    data: status_data0
                },
                yAxis: {
                    name: "人数"
                },
                series: [{
                    name: '人数',
                    type: 'bar',
                    data: this.count_data
                }]
            });

            window.addEventListener("resize",function(){
                    myChart.resize();
                });
                    }
                }
}
</script>



<style lang="scss" scoped>
.time {
    font-size: 13px;
    color: #999;
  }
  
  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .chart {
    width: 100%;
    display: block;
  }

  .clearfix:before,
  .clearfix:after {
      display: table;
      content: "";
  }
  
  .clearfix:after {
      clear: both
  }

  .flowTitle{
      margin: 20px auto 40px;
      text-align: center;
  }
</style>


