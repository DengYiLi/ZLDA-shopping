<template>
    <div class="home">
        <h3 class="text-center">数据统计</h3>
        <div id="pendingOrder">
            <el-badge :value="12" class="item">
                <el-button size="small">待处理订单</el-button>
            </el-badge>
        </div>
    </div>
</template>
<style>
    .home{
        margin-top: 25px;
    }
</style>