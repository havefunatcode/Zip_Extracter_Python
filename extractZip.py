import os
import zipfile

def extractZipFile(filePath):

    os.chdir(filePath)          # GUI에서 넘겨받은 파일 디렉토리로 이동한다.

    for (root, dirs, files) in os.walk(filePath):
        os.chdir(root)
        if len(files) > 0:  # root의 하위 파일들을 출력하는 부분
            for file_name in files:
                if '.zip' in file_name:  # zip파일인지 확인하는 부분
                    with zipfile.ZipFile(file_name, 'r') as zf:     # zip파일을 압축 해제 하는 경우에 한글이 깨지는 경우를 방지
                        zipInfo = zf.infolist()                     # zip파일의 정보를 가져옴
                        for member in zipInfo:
                            try:
                                print(root)                         # 현재 작업중인 디렉토리명 출력
                                member.filename = member.filename.encode('cp437').decode('euc-kr', 'ignore')    # 한글 깨짐 방지
                                print(member.filename)              # cp437로 인코딩되고 euc-kr로 디코딩된 파일 이름 출력
                                zf.extract(member, root)
                            except UnicodeEncodeError as e:         # cp437로 encode가 안되는 경우 -> utf-8로 encode
                                member.filename = member.filename.encode('utf-8').decode('utf-8', 'ignore')     # 한글 깨짐 방지
                                print(member.filename)              # utf-8로 인코딩되고 utf-8로 디코딩된 파일 이름 출력
                                zf.extract(member, root)
                            except:                                 # 그 외에 발생하는 부분에 대한 예외처리
                                raise Exception('Can\'t extract zip file.')
                    os.remove(file_name)  # 압축 해제 완료된 zip파일 삭제