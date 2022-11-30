import { defineConfig } from '@umijs/max';

export default defineConfig({
  antd: {},
  access: {},
  model: {},
  initialState: {},
  request: {},
  layout: {
    title: 'Jethro',
  },
  routes: [
    {
      path: '/',
      redirect: '/home',
    },
    {
      name: 'Home',
      path: '/home',
      component: './Home',
    },
    {
      name: 'Service Schedule',
      path: '/service',
      component: './Access',
    },
    {
      name: 'CRUD Example',
      path: '/crud',
      component: './Table',
      hideInMenu: true,
    },
  ],
  npmClient: 'yarn',
});
