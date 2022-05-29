

```cpp
// 主窗口类名
WCHAR CLASS_NAME[] = "这里是主窗口类名"

// 调用消息目标窗口的窗口过程
DispatchMessage(&msg);

// 窗口过程
LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam);

// 默认消息传递
// 如果不在窗口过程中处理特定消息，请将消息参数直接传递给 DefWindowProc 函数
return DefWindowProc(hwnd, uMsg, wParam, lParam);

// 窗口
LRESULT CALLBACK    WndProc(HWND, UINT, WPARAM, LPARAM);

```









