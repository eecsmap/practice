import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JOptionPane;

public final class DemoApp {

    public static void main(String... args) {
        // JFrame代表基本窗口，提供标题，窗口大小
        JFrame frame = new JFrame("title");
        // 默认的关闭行为只是隐藏
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // JPanel代表绘制区域，有一个双缓冲，一个基本的layout
        JPanel panel = new JPanel();
        frame.getContentPane().add(panel);
        panel.add(new JLabel("hello world!"));
        JButton button = new JButton("OK");
        panel.add(button);
        button.addActionListener(event -> JOptionPane.showMessageDialog(frame, "message is here!"));
        // 通过pack来计算窗口的实际大小
        frame.pack();
        frame.setVisible(true);
    }
}