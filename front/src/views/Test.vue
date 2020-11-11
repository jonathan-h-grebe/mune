<template>
  <div class="test">
    <table>
      <tr>
        <th>名前</th>
        <th>ステータス</th>
        <th>高さ</th>
        <th>幅</th>
        <th>奥行き</th>
        <th>作成者</th>
        <th>作成日時</th>
      </tr>
      <tr v-for="(item, key) in Items" :key="key">
        <td>{{ item.name }}</td>
        <td>{{ item.status }}</td>
        <td>{{ item.height }}</td>
        <td>{{ item.width }}</td>
        <td>{{ item.depth }}</td>
        <td>{{ item.created_by }}</td>
        <td>{{ item.created_at}}</td>
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
      Items: []
    };
  },
  mounted() {
    this.axios
      .get("http://127.0.0.1:8081/api/item/")
      .then(response => {
        //var res = JSON.parse()
        for (var r in response.data.results){
            var item = response.data.results[r];
            this.Items.push(item);
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

