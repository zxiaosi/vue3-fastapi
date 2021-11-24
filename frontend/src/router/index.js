import { createRouter, createWebHashHistory } from "vue-router";
import Home from "../views/Home.vue";

const routes = [
    { path: '/', redirect: '/dashboard' }, // 重定向
    {
        path: "/", name: "Home", component: Home,
        children: [
            {
                path: "/dashboard", name: "dashboard", meta: { title: '系统首页' },
                component: () => import( /* webpackChunkName: "dashboard" */ "../views/Dashboard.vue")
            },
            {
                path: "/department", name: "department", meta: { title: '院系表' },
                component: () => import( /* webpackChunkName: "department" */ "../views/tables/Department.vue")
            },
            {
                path: "/major", name: "major", meta: { title: '专业表' },
                component: () => import( /* webpackChunkName: "major" */ "../views/tables/Major.vue")
            },
            {
                path: "/teacher", name: "teacher", meta: { title: '教师表' },
                component: () => import( /* webpackChunkName: "teacher" */ "../views/tables/Teacher.vue")
            },
            {
                path: "/student", name: "student", meta: { title: '学生表' },
                component: () => import( /* webpackChunkName: "student" */ "../views/tables/Student.vue")
            },
            {
                path: "/course", name: "course", meta: { title: '课程表' },
                component: () => import( /* webpackChunkName: "course" */ "../views/tables/Course.vue")
            },
            {
                path: "/selectcourse", name: "selectcourse", meta: { title: '选课表' },
                component: () => import( /* webpackChunkName: "selectcourse" */ "../views/tables/SelectCourse.vue")
            },
            {
                path: "/basetable", name: "basetable", meta: { title: '基础表格' },
                component: () => import( /* webpackChunkName: "basetable" */ "../views/tables/BaseTable.vue")
            },
            {
                path: "/baseform", name: "baseform", meta: { title: '基本表单' },
                component: () => import( /* webpackChunkName: "baseform" */ "../views/BaseForm.vue")
            },
            {
                path: "/tabs", name: "tabs", meta: { title: 'tab标签' },
                component: () => import( /* webpackChunkName: "tabs" */ "../views/Tabs.vue")
            },
            {
                path: "/permission", name: "permission", meta: { title: '权限管理', permission: true },
                component: () => import( /* webpackChunkName: "permission" */ "../views/Permission.vue")
            },
            {
                path: '/404', name: '404', meta: { title: '找不到页面' },
                component: () => import(/* webpackChunkName: "404" */ '../views/404.vue')
            },
            {
                path: '/403', name: '403', meta: { title: '没有权限' },
                component: () => import(/* webpackChunkName: "403" */ '../views/403.vue')
            },
            {
                path: "/test", name: "test", meta: { title: '测试页面' },
                component: () => import( /* webpackChunkName: "test" */ "../views/Test.vue")
            },
        ]
    },
    {
        path: "/login", name: "Login", meta: { title: '登录' },
        component: () => import( /* webpackChunkName: "login" */ "../views/Login.vue")
    }
];

const router = createRouter({
    history: createWebHashHistory(),
    routes
});

router.beforeEach((to, from, next) => {
    document.title = `${to.meta.title} | ${TITLE}`;
    const role = localStorage.getItem('ms_username');
    if (!role && to.path !== '/login') {
        next('/login');
    } else if (to.meta.permission) {
        // 如果是管理员权限则可进入，这里只是简单的模拟管理员权限而已
        role === 'admin'
            ? next()
            : next('/403');
    } else {
        next();
    }
});

export default router;