
<template>
  <div>
    <h1>
      Simple Views Counter
    </h1>
    <h1>Counter amount: {{ views }}</h1>
  </div>

  
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      views: 0
    }
  },
  async mounted() {
    const counter = await axios.get("http://localhost:8001/api/views-counter/")
    console.log(counter.data.my_count);
    this.views = counter.data.my_count;
  }
}
</script>
