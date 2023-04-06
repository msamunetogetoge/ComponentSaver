<template>
    <v-card :height="'800px'">
        <v-card-text :height="'600px'">
            <MonacoEditor v-model="value" lang="vue" :options="{ theme: 'vs-dark' }"
                v-bind:style="{ width: ' 100%', height: '500px' }" />
        </v-card-text>
    </v-card>
</template>
  

<script lang="ts" setup>
import { useRoute } from 'vue-router';


const route = useRoute();

// サーバーからVueファイルの内容を取得
const name = route.params.name// パスパラメータからidを取得
const componentData = await fetch('http://localhost:5000/components/' + name).then((response) => { return response.json() }).catch((error) => {

    throw createError({
        statusCode: 404,
        message: "コンポーネントが存在しません",
        fatal: true,
    });
})

const value = componentData.component_content;

</script>

<!-- <script lang="ts">
import { defineComponent, ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

// https://blog.mamansoft.net/2018/07/16/nuxtjs-typescript-monacoeditor/#%E3%83%84%E3%83%BC%E3%83%AB%E3%81%AE%E3%83%87%E3%83%A2 で解決できそう

export default defineComponent({
    /**
     * /{id}でゲットリクエストを貰う事で、バックエンドにデータを取得しに行く。
     * 取得したデータからコンポーネントのデータ部分を読み込み、表示する。
     */

    name: 'ComponentLoader',

    setup() {
        const dynamicComponent = ref(null);
        const route = useRoute();
        const theme = "vs-dark"

        // onMounted(async () => {
        //     // サーバーからVueファイルの内容を取得
        //     const name = route.params.name// パスパラメータからidを取得
        //     const componentData = await fetch('http://localhost:5000/components/' + name).then((response) => { return response.json() }).catch((error) => {
        //         console.error(error);
        //         return ""
        //         // throw createError({
        //         //     statusCode: 404,
        //         //     message: "コンポーネントが存在しません",
        //         //     fatal: true,
        //         // });
        //     })


        // 取得したコードをVueコンポーネントとして登録

        // });

        return {
            dynamicComponent,
            theme
        };
    },
    data() {
        return {
            code: "const noop = () => {}",

        };
    }
});
</script> -->