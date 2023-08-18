#!/usr/bin/env python
import sys

import rclpy

from ros_tcp_endpoint import TcpServer


def main(args=None):
    rclpy.init(args=args)
    tcp_server = TcpServer("UnityEndpoint")

    tcp_server.start()

    try:
        tcp_server.setup_executor()
    except KeyboardInterrupt:
        pass
    except BaseException:
        tcp_server.logerr(f'Exception: {sys.exc_info()}')
    finally:
        tcp_server.destroy_nodes()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
