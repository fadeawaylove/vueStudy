import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

// 用于存储数据
var state = {
  // 是否登录
  isLogin: false
}

// 用于存储方法
var mutations = {
    updateUserStatus()
    {

    }
}

// 获取属性, 属性变化的时候就会自己变化
var getters = {
  //获取登录状态
    computedStatus: (state) => {
        return state.isLogin
    }
}

// 异步操作
var actions = {
//   获取登录状态
  setUser({ commit }, flag) {
    commit('userStatus', flag)
  }
}

// 实例化一个Vuex的store
const store = new Vuex.Store({
  state: state,
  mutations: mutations,
  getters: getters,
  actions: actions
})

export default store
