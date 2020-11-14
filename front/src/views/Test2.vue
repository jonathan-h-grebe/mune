<template>
  <div class="test">
    <table class="table">
      <tr>
        <th>問い合わせ種別</th>
        <th>ステータス</th>
        <th>商品</th>
        <th>氏名</th>
        <th>メールアドレス</th>
        <th>作成者</th>
        <th>作成日時</th>
      </tr>
      <tr v-for="(obj, key) in Objects" :key="key">
        <td>{{ obj.case_type.name }}</td>
        <td>{{ obj.status }}</td>
        <td>
          <p v-for="(item, key) in obj.item_list" :key="key">
            {{key}}, {{item.name}}
          </p>
        </td>
        <td>{{ obj.user_name }}</td>
        <td>{{ obj.mail_address }}</td>
        <td>{{ obj.created_by }}</td>
        <td>{{ obj.created_at}}</td>
      </tr>
    </table>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import HelloWorld from '@/components/HelloWorld.vue'; // @ is an alias to /src

@Component({
  components: {
    HelloWorld,
  },
})
export default class Home extends Vue {}
</script>

<script>
export default {
  data() {
    return {
      Objects: []
    };
  },
  mounted() {
    this.axios
      .get("http://127.0.0.1:8081/api/case/")
      .then(response => {
        //var res = JSON.parse()
        for (var r in response.data.results){
            var obj = response.data.results[r];
            this.Objects.push(obj);
        }
      })
      .catch(e => {
        console.error(e)
        console.error("TES")
        this.Items = [
            {
                "name":e,
                "height": e.response,
            }
        ]
      });
  }
};
</script>

