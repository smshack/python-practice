import grpc
import RelayServerRPC_pb2
import RelayServerRPC_pb2_grpc
import MicrophoneStream as MS
from ctypes import *

RATE = 16000
CHUNK = int(RATE / 10)  

RATE = 16000
CHUNK = int(RATE / 10)  # 100ms
def generate_request():
    with MS.MicrophoneStream(RATE, CHUNK) as stream:
        audio_generator = stream.generator()
        for content in audio_generator:
            message = RelayServerRPC_pb2.reqSpeech()
            message.audioContent = content
            # print(message)
            yield message


def STT():
    print("\n\n음성인식 시작")
    channel = grpc.insecure_channel('localhost:50050')
    stub = RelayServerRPC_pb2_grpc.RelayServerStub(channel)
    request = generate_request()
    
    response = stub.STT(request)
    resultCd = response.resultCd
    recogText = response.text

    print(f"인식결과: {recogText}\n\n")
    return recogText


if __name__ == '__main__':
    STT()