# Copyright The Caikit Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Standard
from os import path
import sys

# First Party
import alog

# Here we assume that `start_runtime` file is at the same level of the `text_sentiment` package
sys.path.append(
   path.abspath(path.join(path.dirname(__file__), "../"))
)

# Local
import text_sentiment

alog.configure(default_level="debug")

# Local
from caikit.runtime import grpc_server

# Start the gRPC Caikit runtime server
grpc_server.main()


$ python3 start_runtime.py

<function register_backend_type at 0x7fce0064b5e0> is still in the BETA phase and subject to change!
{"channel": "COM-LIB-INIT", "exception": null, "level": "info", "log_code": "<RUN11997772I>", "message": "Loading service module: text_sentiment", "num_indent": 0, "thread_id": 8605140480, "timestamp": "2023-05-02T11:42:52.808812"}
{"channel": "COM-LIB-INIT", "exception": null, "level": "info", "log_code": "<RUN11997772I>", "message": "Loading service module: caikit.interfaces.common", "num_indent": 0, "thread_id": 8605140480, "timestamp": "2023-05-02T11:42:52.809406"}
{"channel": "COM-LIB-INIT", "exception": null, "level": "info", "log_code": "<RUN11997772I>", "message": "Loading service module: caikit.interfaces.runtime", "num_indent": 0, "thread_id": 8605140480, "timestamp": "2023-05-02T11:42:52.809565"}
[杊{"channel": "MODEL-LOADER", "exception": null, "level": "info", "log_code": "<RUN89711114I>", "message": "Loading model text_sentiment'", "num_indent": 0, "thread_id": 8605140480, "timestamp": "2023-05-02T11:42:52.826657"}
{"channel": "MDLMNG", "exception": null, "level": "warning", "log_code": "<COR56759744W>", "message": "No backend configured! Trying to configure using default config file.", "num_indent": 0, "thread_id": 8605140480, "timestamp": "2023-05-02T11:42:52.827742"}
No model was supplied, defaulted to distilbert-base-uncased-finetuned-sst-2-english and revision af0f99b (https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english).
Using a pipeline without specifying a model name and revision in production is not recommended.
[杊{"channel": "COM-LIB-INIT", "exception": null, "level": "info", "log_code": "<RUN11997772I>", "message": "Loading service module: text_sentiment", "num_indent": 0, "thread_id": 8605140480, "timestamp": "2023-05-02T11:42:53.929756"}
{"channel": "COM-LIB-INIT", "exception": null, "level": "info", "log_code": "<RUN11997772I>", "message": "Loading service module: caikit.interfaces.common", "num_indent": 0, "thread_id": 8605140480, "timestamp": "2023-05-02T11:42:53.929814"}
{"channel": "COM-LIB-INIT", "exception": null, "level": "info", "log_code": "<RUN11997772I>", "message": "Loading service module: caikit.interfaces.runtime", "num_indent": 0, "thread_id": 8605140480, "timestamp": "2023-05-02T11:42:53.929858"}
{"channel": "GP-SERVICR-I", "exception": null, "level": "info", "log_code": "<RUN76773778I>", "message": "Validated Caikit Library CDM successfully", "num_indent": 0, "thread_id": 8605140480, "timestamp": "2023-05-02T11:42:53.929942"}
{"channel": "GP-SERVICR-I", "exception": null, "level": "info", "log_code": "<RUN76884779I>", "message": "Constructed inference service for library: text_sentiment, version: unknown", "num_indent": 0, "thread_id": 8605140480, "timestamp": "2023-05-02T11:42:53.930734"}
{"channel": "SERVER-WRAPR", "exception": null, "level": "info", "log_code": "<RUN81194024I>", "message": "Intercepting RPC method /caikit.runtime.HfTextsentiment.HfTextsentimentService/HfBlockPredict", "num_indent": 0, "thread_id": 8605140480, "timestamp": "2023-05-02T11:42:53.930786"}
{"channel": "SERVER-WRAPR", "exception": null, "level": "info", "log_code": "<RUN33333123I>", "message": "Wrapping safe rpc for Predict", "num_indent": 0, "thread_id": 8605140480, "timestamp": "2023-05-02T11:42:53.931424"}
{"channel": "SERVER-WRAPR", "exception": null, "level": "info", "log_code": "<RUN30032825I>", "message": "Re-routing RPC /caikit.runtime.HfTextsentiment.HfTextsentimentService/HfBlockPredict from <function _ServiceBuilder._GenerateNonImplementedMethod.<locals>.<lambda> at 0x7fce01f660d0> to <function CaikitRuntimeServerWrapper.safe_rpc_wrapper.<locals>.safe_rpc_call at 0x7fce02144670>", "num_indent": 0, "thread_id": 8605140480, "timestamp": "2023-05-02T11:42:53.931479"}
{"channel": "SERVER-WRAPR", "exception": null, "level": "info", "log_code": "<RUN24924908I>", "message": "Interception of service caikit.runtime.HfTextsentiment.HfTextsentimentService complete", "num_indent": 0, "thread_id": 8605140480, "timestamp": "2023-05-02T11:42:53.931530"}
[杊
{"channel": "GRPC-SERVR", "exception": null, "level": "info", "log_code": "<RUN10001807I>", "message": "Running in insecure mode", "num_indent": 0, "thread_id": 8605140480, "timestamp": "2023-05-02T11:42:53.936511"}
{"channel": "GRPC-SERVR", "exception": null, "level": "info", "log_code": "<RUN10001001I>", "message": "Caikit Runtime is serving on port: 8085 with thread pool size: 5", "num_indent": 0, "thread_id": 8605140480, "timestamp": "2023-05-02T11:42:53.938054"}