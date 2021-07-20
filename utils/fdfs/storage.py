from django.core.files.storage import Storage
from fdfs_client.client import Fdfs_client
import os
import re

from tempfile import NamedTemporaryFile


class FDFSStorage(Storage):
    """FAST DFS 文件存储类"""

    def _open(self, name, mode='rb'):
        """打开文件时使用"""
        pass

    def _save(self, content):
        """保存文件时使用"""
        # name:你选择上传文件的名字
        # content:包含你上传文件内容的file对象，有这个对象后就能获取文件的内容

        # 创建一个Fdfs—client对象
        client = Fdfs_client('/etc/fdfs/client.conf')
        # 创建临时文件，结局内存溢出
        if re.match(r'.mp4', '%s' % content):
            with NamedTemporaryFile('w+b', dir='temporary_file', delete=False, suffix='.mp4') as f:
                while True:
                    line = content.read(2048)
                    f.write(line)
                    if not line:
                        break
        else:
            with NamedTemporaryFile('w+b', dir='temporary_file', delete=False) as f:
                while True:
                    line = content.read()
                    f.write(line)
                    if not line:
                        break
            # 上传文件到fast
        res = client.upload_by_filename(f.name)
        # upload_by_buffer返回的内容 是字典：Status判断上传是否失败， Remote file_id文件在fast dfs文件系统中的ID
        # {
        #     'Group name': group_name,
        #     'Remote file_id': remote_file_id,
        #     'Status': 'Upload successed.',
        #     'Local file name': '',
        #     'Uploaded size': upload_size,
        #     'Storage IP': storage_ip
        # } if success else None

        if res.get('Status') != 'Upload successed.':
            # 上传失败
            raise Exception('上传文件失败')
        file_name = res.get('Remote file_id')
        os.remove(f.name)
        return file_name

    def exists(self, name):
        """Django判断文件名是否可用"""
        return False

    def url(self, name):
        """返回访问文件的URL路径"""
        return 'http://192.168.101.121:8888/' + name
