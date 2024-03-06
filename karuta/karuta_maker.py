from PIL import Image

def split_and_save_image(input_path, num,output_path="fuda", rows=2, cols=4):
    fuda_top=["あ","い","う","え","お","か","き","く","け","こ","さ","し",
              "す","せ","そ","た","ち","つ","て","と","な","に","ぬ","ね",
              "の","は","ひ","ふ","へ","ほ","ま","み","む","め","も","や","ゆ","よ","ら","り","る","れ","ろ","わ","を","ん"]
    # 画像を開く
    img = Image.open(input_path)
    
    # 画像のサイズを取得
    width, height = img.size
    
    # 分割後のサイズを計算
    cell_width = width // cols
    cell_height = height // rows
    
    # 分割して保存
    for row in range(rows):
        for col in range(cols):
            # 分割した領域を取得
            left = col * cell_width
            top = row * cell_height
            right = (col + 1) * cell_width
            bottom = (row + 1) * cell_height
            
            # 分割した領域をクロップ
            cell_img = img.crop((left, top, right, bottom))
            
            # 保存するファイル名を生成
            p="read"
            if row == 0:
                cell_img = cell_img.transpose(Image.FLIP_TOP_BOTTOM).transpose(Image.FLIP_LEFT_RIGHT)
            if row>0:
                p="show"
            num1=num*4+col+20
            if num1<len(fuda_top):
                output_file = f"{output_path}/{p}/{fuda_top[num1]}.jpeg"
            
                # 分割した領域を保存
                cell_img.save(output_file)

if __name__ == "__main__":
    # 入力と出力のパスを指定
    for i in range(7):
        input_image_path = f"t{i}.jpeg"
        split_and_save_image(input_image_path,i)