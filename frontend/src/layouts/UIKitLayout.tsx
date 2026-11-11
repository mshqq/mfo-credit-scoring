import { Flex, Layout, Anchor, Typography } from 'antd';
import { Content } from 'antd/es/layout/layout';
import Sider from 'antd/es/layout/Sider';
import { Outlet } from 'react-router-dom';
import { uiKitSections } from '../config/UIKitSections';

const menuItems = uiKitSections.map(({ id, label, icon: Icon }) => ({
  key: id,
  href: `#${id}`,
  title: (
    <Flex align="center" gap={8} style={{ padding: '5px 0' }} component="span">
      <Icon strokeWidth={1.6} />
      <Typography.Text>{label}</Typography.Text>
    </Flex>
  ),
}));

export default function UIKitLayout() {
  return (
    <Layout hasSider className="min-h-dvh bg-gray-50">
      <Sider
        width={260}
        theme="light"
        className="h-dvh border-r border-gray-100"
        style={{ background: '#fff', position: 'sticky', top: 0 }}
      >
        <div className="flex flex-col h-full">
          <a href="#overview" className="flex items-center gap-3 px-6 py-8">
            <div className="w-8 h-8 bg-pink-300 rounded-full flex items-center justify-center">
              🌸
            </div>
            <div className="flex flex-col leading-none">
              <strong className="text-xl font-bold text-gray-900">FINO</strong>
              <span className="text-xs text-gray-500 mt-1">Design System</span>
            </div>
          </a>
          <div className="flex-1 overflow-y-auto custom-menu">
            <Anchor affix={false} items={menuItems} targetOffset={24} />
          </div>
          <div className="p-4 mt-auto">
            <div className="relative overflow-hidden rounded-2xl bg-linear-to-br from-pink-50 via-pink-100 to-pink-200 p-5">
              <div className="relative z-10">
                <div className="text-lg font-bold text-pink-700 mb-2">
                  <span className="text-gray-900">FINO</span> UI Kit
                </div>
                <p className="text-sm text-gray-600 leading-tight">
                  Дизайн-система <br />
                  для всех продуктов <br />
                  FINO.
                </p>
              </div>
            </div>
          </div>
        </div>
      </Sider>

      <Content>
        <main className="p-8 bg-pink-300/30">
          <Outlet />
        </main>
      </Content>
    </Layout>
  );
}
