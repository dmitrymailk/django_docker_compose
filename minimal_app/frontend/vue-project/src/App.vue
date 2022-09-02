<template>
  <div>
    <h1>Simple Views Counter</h1>
    <h1>Current date {{ current_date }}</h1>
    <h1>Counter amount: {{ views }}</h1>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      views: 0,
      current_date: "- - -",
    };
  },
  async mounted() {
    const domain = import.meta.env.VITE_DOMAIN;
    console.log(domain);

    const counter = await axios.get(`${domain}/api/views-counter/`);
    console.log(counter.data);
    this.views = counter.data.my_count;
    this.current_date = counter.data.current_date;
  },
};
</script>
