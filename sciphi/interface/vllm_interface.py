"""A module for interfacing with local vLLM models"""
import logging
from typing import List

from sciphi.interface.base import LLMInterface, ProviderName
from sciphi.interface.interface_manager import llm_provider
from sciphi.llm import vLLM, vLLMConfig

logger = logging.getLogger(__name__)


@llm_provider
class vLLMInterface(LLMInterface):
    """A class to interface with local vLLM models."""

    provider_name = ProviderName.VLLM

    def __init__(
        self,
        config: vLLMConfig = vLLMConfig(),
    ) -> None:
        self._model = vLLM(config)

    def get_completion(self, prompt: str) -> str:
        """Get a completion from the local vLLM provider."""

        logger.debug(
            f"Requesting completion from local vLLM with model={self._model.config.model_name} and prompt={prompt}"
        )
        return self.model.get_instruct_completion(prompt)

    def get_batch_completion(self, prompts: List[str]) -> List[str]:
        """Get a completion from the local vLLM provider."""

        logger.debug(
            f"Requesting completion from local vLLM with model={self._model.config.model_name} and prompts={prompts}"
        )
        return self.model.get_batch_instruct_completion(prompts)

    @property
    def model(self) -> vLLM:
        return self._model
