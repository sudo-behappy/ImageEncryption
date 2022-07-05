
# ImageEncryption

基于RSA的一个图片加密器

## 使用方法

前往工程文件夹

```bash
cd ImageEncryption
```

先运行RSA.py利用你自己的质数生成公钥和私钥, 如果质数过大, 生成过程会比较长

> 笔者使用(10061, 10067), 生成时间 ~= 4s
>
> 公钥: (3, 101284087)
>
> 私钥: (50631980, 101284087)

```bash
python RSA.py keygen
```

**质数对至少是(17, 19), 否则无法加密图片**

### 加密

生成完公钥和私钥后, 将encrypt.py, RSA.py 和公钥发给你的朋友, 放在同一目录下.

让他运行encrypt.py, 并输入图片路径和你提供的公钥, 如果图片不存在, 就会报错.

```bash
python encrypt.py
```

运行完成后(4343*6080图像差不多30秒, 取决于你所提供的质数大小)会生成encrypted.npz文件. 叫他把这个文件发送给你.

### 解密

运行decrypt.py, 并输入你的私钥和npz文件路径.

```bash
python decrypt.py
```

会在文件路径输出一个解密后的图片decrypted.png.
