<template>
  <div>
    <component :is="dynamicComponent" v-if="dynamicComponent" />
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue';

export default defineComponent({
  name: 'DynamicComponentLoader',
  setup() {
    const dynamicComponent = ref(null);

    onMounted(async () => {
      // サーバーからVueファイルの内容を取得
      const response = await fetch('/components/your_component_name');
      const componentData = await response.json();

      // 取得したコードをVueコンポーネントとして登録
      const componentCode = componentData.component_content;
      dynamicComponent.value = new Function('return ' + componentCode)();
    });

    return {
      dynamicComponent,
    };
  },
});
</script>
