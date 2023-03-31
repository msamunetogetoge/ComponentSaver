<!-- <template>
  <div>
    <NuxtWelcome />
  </div>
</template> -->
<template>
  <div>
    <component :is="dynamicComponent" />
  </div>
</template>

<script>
export default {
  data() {
    return {
      dynamicComponent: null,
    };
  },
  async mounted() {
    // サーバーからVueファイルの内容を取得
    const response = await this.$axios.get("/components/your_component_name");
    const componentCode = response.data;

    // 取得したコードをVueコンポーネントとして登録
    this.dynamicComponent = new Function("return " + componentCode)();
  },
};
</script>
