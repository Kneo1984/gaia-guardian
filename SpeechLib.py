# -*- coding: utf-8 -*-
from enum import IntFlag

import comtypes.gen._C866CA3A_32F7_11D2_9602_00C04F8EE628_0_5_4 as __wrapper_module__
from comtypes.gen._C866CA3A_32F7_11D2_9602_00C04F8EE628_0_5_4 import (
    DISPID_SPRuleParent, SpVoice, SVP_17, ISpStream,
    DISPID_SPAPhraseInfo, SAFT16kHz16BitMono, ISpVoice,
    DISPID_SVAlertBoundary, SVP_6, DISPID_SPCIdToPhone,
    ISpRecoContext2, SPINTERFERENCE_NONE, DISPID_SVSkip,
    DISPID_SRGDictationLoad, DISPID_SRCEPropertyNumberChange,
    DISPID_SPAsCount, DISPID_SPEAudioStreamOffset, SP_VISEME_10,
    DISPID_SRGCmdLoadFromObject, SPCS_DISABLED, SPSEMANTICERRORINFO,
    ISpeechFileStream, SDA_Consume_Leading_Spaces, SECFIgnoreWidth,
    SPINTERFERENCE_NOSIGNAL, DISPID_SPEAudioTimeOffset,
    DISPID_SRRAudio, DISPID_SVResume, SWTDeleted, SPPS_Interjection,
    eWORDTYPE_ADDED, DISPID_SPERequiredConfidence, ISpeechRecognizer,
    DISPID_SASState, SPEI_VISEME, DISPID_SVVoice, ISpNotifySource,
    DISPID_SRRPhraseInfo, DISPID_SLWType, eLEXTYPE_PRIVATE6,
    DISPID_SRCState, DISPID_SRSetPropertyNumber, STSF_FlagCreate,
    DISPID_SVSVisemeId, SP_VISEME_13, SpeechAudioFormatGUIDWave,
    DISPID_SGRsAdd, SAFT24kHz16BitMono, SPEI_SR_RETAINEDAUDIO,
    SAFT12kHz16BitStereo, SPAUDIOSTATUS,
    DISPID_SPIAudioStreamPosition, SPWT_LEXICAL,
    DISPID_SGRSTs_NewEnum, CoClass, SLODynamic, SINoise,
    SPSMF_SRGS_SAPIPROPERTIES, SpeechCategoryAudioOut,
    eLEXTYPE_MORPHOLOGY, SpeechGrammarTagDictation, SPSUnknown,
    DISPID_SRCRequestedUIType, SPAS_RUN, SVSFPersistXML,
    DISPID_SRSSupportedLanguages, DISPID_SRCERecognition, SVP_7,
    SGDSInactive, SPEI_RESERVED1, SPBO_AHEAD, DISPID_SAFGuid,
    SGRSTTDictation, SAFTCCITT_uLaw_8kHzMono, SRATopLevel,
    SPPHRASERULE, DISPID_SLGenerationId, SPAUDIOBUFFERINFO,
    DISPID_SPEEngineConfidence, eLEXTYPE_PRIVATE10, DISPID_SPRsCount,
    DISPID_SFSClose, SVSFDefault, DISPID_SVEBookmark,
    SpeechAudioProperties, SAFT12kHz16BitMono, SP_VISEME_20,
    SpPhoneticAlphabetConverter, DISPID_SPCLangId,
    DISPID_SPRFirstElement, IEnumString, DISPID_SPPsCount, SPAR_Low,
    SpSharedRecoContext, SAFT44kHz16BitStereo, DISPID_SPIElements,
    SPPHRASEPROPERTY, ISpNotifySink, ISpPhoneticAlphabetConverter,
    DISPID_SVGetProfiles, DISPID_SRAudioInputStream,
    SPEI_START_SR_STREAM, ISpRecoContext, DISPID_SPPFirstElement,
    DISPID_SOTMatchesAttributes, SPEVENTSOURCEINFO,
    DISPID_SPISaveToMemory, DISPID_SPPsItem, ISpPhrase,
    SpeechPropertyAdaptationOn, ISpRecognizer, SPXRO_SML,
    DISPID_SGRAttributes, SRAExport, SVP_5, STCRemoteServer,
    DISPID_SLWsCount, SPWORDPRONUNCIATION, SpeechMicTraining,
    DISPMETHOD, DISPID_SRCEBookmark, SpMMAudioEnum,
    SpeechTokenKeyFiles, SRSInactive, DISPID_SPRuleConfidence,
    DISPID_SPIEngineId, SVSFIsXML, SpShortcut,
    DISPID_SRGSetTextSelection, SPSHORTCUTPAIRLIST, SAFT8kHz8BitMono,
    SSSPTRelativeToStart, eLEXTYPE_USER_SHORTCUT, SRAONone,
    SpeechCategoryPhoneConverters, DISPID_SRGId,
    SpeechRegistryLocalMachineRoot, SPLO_STATIC,
    ISpeechGrammarRuleStateTransition, ISpeechObjectTokenCategory,
    DISPID_SRCERecognizerStateChange, DISPID_SRCESoundEnd, COMMETHOD,
    DISPID_SGRName, SPCT_SLEEP, eLEXTYPE_PRIVATE3, ISpXMLRecoResult,
    SPPHRASE, DISPID_SPIProperties, SVP_10, SAFT11kHz8BitMono,
    SDA_No_Trailing_Space, SASPause,
    DISPID_SPANumberOfElementsInResult, SPEI_SR_BOOKMARK,
    ISpeechVoiceStatus, SPEI_START_INPUT_STREAM, SVSFParseSsml,
    SWPKnownWordPronounceable, SGDSActiveWithAutoPause, ISpEventSink,
    DISPID_SRCRetainedAudio, SREAdaptation, DISPIDSPTSI_ActiveOffset,
    DISPID_SDKDeleteValue, SPCT_DICTATION, SVEEndInputStream,
    DISPID_SPPParent, ISpDataKey, SRSActive, SPSHT_EMAIL,
    ISpeechLexiconWord, ISpeechPhraseProperty, SPSNotOverriden,
    SVEVoiceChange, SAFT48kHz8BitMono, IUnknown,
    SAFTADPCM_22kHzStereo, SDTPronunciation, SPPS_Modifier,
    ISpeechPhraseRules, tagSPPROPERTYINFO, SVP_18, SDTAudio,
    DISPID_SVAudioOutput, _check_version, STCInprocHandler,
    SPWP_UNKNOWN_WORD_UNPRONOUNCEABLE, SAFTGSM610_11kHzMono,
    ISpeechAudio, SPDKL_DefaultLocation, DISPID_SGRSTsCount,
    ISpObjectTokenCategory, DISPID_SVSyncronousSpeakTimeout,
    DISPID_SRSAudioStatus, DISPID_SVSpeakCompleteEvent, SPSMF_UPS,
    IInternetSecurityMgrSite, SpeechPropertyLowConfidenceThreshold,
    DISPID_SOTSetId, DISPID_SOTRemoveStorageFileName, DISPID_SVRate,
    DISPID_SPPEngineConfidence, SGSEnabled, SPFM_CREATE_ALWAYS,
    DISPID_SGRSAddWordTransition, DISPID_SPRs_NewEnum, eLEXTYPE_APP,
    ISpRecognizer3, ISpeechLexiconPronunciation, ISpeechLexicon,
    Speech_Max_Pron_Length, DISPID_SRGState, SAFTNonStandardFormat,
    SDKLCurrentUser, SVP_8, SAFTCCITT_ALaw_22kHzMono, SP_VISEME_15,
    DISPID_SPIRetainedSizeBytes, STCInprocServer, SAFT12kHz8BitStereo,
    SAFTCCITT_uLaw_22kHzStereo, DISPID_SPPs_NewEnum,
    ISpeechPhraseProperties, SPINTERFERENCE_LATENCY_TRUNCATE_END,
    eLEXTYPE_RESERVED10, DISPID_SGRs_NewEnum,
    DISPID_SRGCmdSetRuleIdState, SPEI_END_INPUT_STREAM,
    SPEI_SR_AUDIO_LEVEL, SPEI_END_SR_STREAM, DISPID_SOTCDefault,
    DISPID_SPILanguageId, SDTReplacement, SPAR_Medium,
    SPEI_PROPERTY_NUM_CHANGE, SPRST_NUM_STATES, SPEI_SOUND_START,
    DISPID_SWFEExtraData, SPRST_ACTIVE_ALWAYS, ISpeechAudioFormat,
    DISPID_SBSFormat, wireHWND, SPEI_RESERVED5,
    SPWP_UNKNOWN_WORD_PRONOUNCEABLE, SPPS_RESERVED4,
    SAFTCCITT_ALaw_11kHzStereo, ISpResourceManager,
    DISPIDSPTSI_ActiveLength, SpeechPropertyResourceUsage,
    ISpObjectToken, __MIDL___MIDL_itf_sapi_0000_0020_0001,
    SVSFParseMask, DISPID_SPEAudioSizeBytes, SRESoundStart,
    SAFTADPCM_11kHzStereo, ISpeechPhraseInfoBuilder,
    SAFT11kHz16BitMono, DISPID_SPPConfidence, ISpeechWaveFormatEx,
    SpInProcRecoContext, DISPID_SADefaultFormat, ISpRecoGrammar2,
    ISpeechAudioBufferInfo, SREAudioLevel, SVEWordBoundary,
    DISPID_SGRAddState, DISPID_SRRRecoContext,
    SPINTERFERENCE_TOOQUIET, SPCS_ENABLED, SAFT44kHz16BitMono,
    SpeechRecoProfileProperties, SpeechGrammarTagUnlimitedDictation,
    DISPID_SLWsItem, SECLowConfidence, ISpShortcut,
    ISpPhoneticAlphabetSelection, SP_VISEME_17, SP_VISEME_2,
    SpFileStream, ISpeechGrammarRules, STSF_CommonAppData, SPPS_LMA,
    SPINTERFERENCE_NOISE, DISPID_SWFEFormatTag, SPPS_RESERVED2,
    DISPID_SVEWord, DISPID_SRRSpeakAudio, SRSActiveAlways,
    DISPID_SVAudioOutputStream, DISPID_SVEStreamEnd,
    DISPID_SPAStartElementInResult, DISPID_SRRTLength,
    DISPID_SREmulateRecognition, SREBookmark, eWORDTYPE_DELETED,
    ISpeechVoice, HRESULT, DISPID_SVSRunningState,
    DISPID_SRGDictationSetState, SAFTCCITT_ALaw_11kHzMono, SRSEDone,
    SSFMCreateForWrite, DISPID_SMSGetData, DISPID_SPELexicalForm,
    SPPROPERTYINFO, SECFIgnoreKanaType, SVP_3,
    DISPID_SRGCmdSetRuleState, SPCT_SUB_COMMAND, DISPID_SLWs_NewEnum,
    SP_VISEME_5, DISPID_SVSpeak, eLEXTYPE_PRIVATE19, DISPID_SOTCId,
    SAFTDefault, SRTSMLTimeout, SRCS_Enabled, GUID, DISPID_SVVolume,
    DISPID_SASNonBlockingIO, SVP_13, ISpeechPhraseRule, SREPrivate,
    DISPID_SPAsItem, _FILETIME, SPVPRI_NORMAL, _ISpeechVoiceEvents,
    LONG_PTR, DISPID_SLRemovePronunciation, SpPhraseInfoBuilder,
    DISPID_SPRDisplayAttributes, ISpeechLexiconWords, SBONone,
    SPINTERFERENCE_TOOFAST, SAFTTrueSpeech_8kHz1BitMono,
    DISPID_SRGReset, DISPID_SBSSeek, SVSFVoiceMask, SAFT24kHz8BitMono,
    SAFT12kHz8BitMono, SAFT8kHz8BitStereo, _ULARGE_INTEGER,
    DISPID_SRGCmdLoadFromFile, ISpeechPhraseReplacements,
    SPRST_INACTIVE, eLEXTYPE_PRIVATE4, SPEI_RESERVED2, ISpPhraseAlt,
    SPPS_SuppressWord, ISpeechMMSysAudio, SP_VISEME_1,
    DISPID_SASCurrentDevicePosition,
    DISPID_SRAllowVoiceFormatMatchingOnNextSet, ISpeechPhraseInfo,
    DISPID_SPEPronunciation, DISPID_SPERetainedStreamOffset,
    SAFTCCITT_ALaw_8kHzMono, ISpeechPhraseElement, SPSLMA, SPWORDLIST,
    DISPID_SDKGetBinaryValue, ISpMMSysAudio, SAFT8kHz16BitMono,
    SPDKL_LocalMachine, ISpeechAudioStatus, DISPID_SPPId,
    SpeechCategoryAppLexicons, DISPID_SPIReplacements,
    ISpeechResourceLoader, ISpeechGrammarRuleState, SPEI_REQUEST_UI,
    SVP_21, SPEI_SR_PRIVATE, SDKLLocalMachine, SP_VISEME_21,
    DISPID_SPIAudioSizeBytes, tagSPTEXTSELECTIONINFO, SPEI_MIN_TTS,
    DISPID_SRCreateRecoContext, DISPID_SVEAudioLevel, SVEPhoneme,
    SPEI_INTERFERENCE, DISPID_SRCEPropertyStringChange,
    SpeechCategoryVoices, DISPID_SRCERecognitionForOtherContext,
    SREInterference, SpeechTokenValueCLSID, SGDisplay, SRTReSent,
    DISPID_SRGetRecognizers, SPRULE, DISPID_SVSLastBookmarkId,
    SAFTGSM610_22kHzMono, SPEI_HYPOTHESIS, DISPID_SLWWord, SpLexicon,
    SDTAll, SPINTERFERENCE_TOOLOUD, SDTRule, SPSERIALIZEDPHRASE,
    SREFalseRecognition, SGSDisabled, SPWT_DISPLAY, SRAImport,
    SPPS_Noun, DISPID_SPEAudioSizeTime, SSTTTextBuffer,
    eLEXTYPE_PRIVATE14, eLEXTYPE_PRIVATE2, DISPID_SMSAMMHandle,
    SpCustomStream, SREStreamEnd, SGRSTTWildcard, SPRECOGNIZERSTATUS,
    eLEXTYPE_PRIVATE13, DISPID_SPRuleChildren, SP_VISEME_12,
    SPEI_VOICE_CHANGE, SPEI_RECO_STATE_CHANGE, SAFTADPCM_8kHzStereo,
    DISPID_SRRAlternates, SPVPRI_OVER, DISPID_SRCEAudioLevel,
    DISPID_SPIGrammarId, DISPID_SPRsItem, DISPID_SDKOpenKey,
    SPBO_TIME_UNITS, UINT_PTR, DISPID_SVPause, STSF_LocalAppData,
    SPFM_OPEN_READONLY, DISPID_SPPChildren, SPSInterjection,
    STCLocalServer, DISPID_SGRSAddRuleTransition, dispid, SITooFast,
    ISpLexicon, SPAS_STOP, SECFDefault, WAVEFORMATEX,
    SAFT11kHz16BitStereo, DISPID_SPRuleId, DISPID_SVSpeakStream,
    SVEStartInputStream, SWPUnknownWordUnpronounceable,
    ISequentialStream, DISPID_SRProfile, DISPID_SRCEInterference,
    DISPID_SRGCmdLoadFromProprietaryGrammar,
    DISPID_SRCCreateResultFromMemory, SPAO_NONE, SPRS_ACTIVE,
    SPPS_Unknown, SPINTERFERENCE_LATENCY_TRUNCATE_BEGIN,
    SAFT16kHz8BitMono, DISPID_SRCSetAdaptationData, SPEI_RECOGNITION,
    SAFTCCITT_ALaw_22kHzStereo, SPSERIALIZEDRESULT,
    DISPID_SRCEAdaptation, SVP_20, SVEAllEvents,
    DISPID_SVGetAudioOutputs, SAFTCCITT_uLaw_44kHzStereo,
    DISPID_SBSRead, DISPID_SRRGetXMLResult, DISPID_SPEDisplayText,
    SPEI_RECO_OTHER_CONTEXT, SpeechAudioVolume, SpMMAudioIn,
    DISPID_SPIStartTime, SPPHRASEREPLACEMENT, DISPID_SRGRecoContext,
    ISpRecoGrammar, SREHypothesis, SECFNoSpecialChars,
    SPRST_INACTIVE_WITH_PURGE, DISPID_SRSClsidEngine,
    DISPID_SPPNumberOfElements, SPFM_NUM_MODES,
    DISPID_SRRDiscardResultInfo, SRSInactiveWithPurge,
    SDA_One_Trailing_Space, SGDSActive, SPSModifier, SRESoundEnd,
    SPEI_PROPERTY_STRING_CHANGE, SAFT22kHz16BitMono,
    DISPID_SVSInputSentencePosition, eLEXTYPE_RESERVED9,
    DISPID_SGRsCommit, SITooLoud, SPRS_ACTIVE_USER_DELIMITED,
    DISPID_SPCPhoneToId, DISPID_SVSLastResult, eLEXTYPE_PRIVATE18,
    DISPID_SASCurrentSeekPosition, SAFTADPCM_44kHzStereo,
    SVSFIsFilename, IInternetSecurityManager, DISPID_SVEPhoneme,
    ISpeechLexiconPronunciations, Library, DISPID_SWFEChannels, SVP_1,
    DISPID_SGRsCount, SSFMOpenForRead, SPAS_CLOSED, DISPID_SGRSRule,
    DISPID_SGRSTText, SGLexicalNoSpecialChars, SVEBookmark,
    DISPID_SPERetainedSizeBytes, ISpSerializeState, STSF_AppData,
    DISPID_SABIEventBias, SPEVENT, __MIDL_IWinTypes_0009, SVP_16,
    SPRS_ACTIVE_WITH_AUTO_PAUSE, SDA_Two_Trailing_Spaces,
    ISpObjectWithToken,
    DISPID_SVAllowAudioOuputFormatChangesOnNextSet,
    DISPIDSPTSI_SelectionLength, SRTStandard, DISPID_SPIAudioSizeTime,
    Speech_StreamPos_Asap, SSFMCreate, DISPID_SGRSTsItem, SP_VISEME_4,
    SRTEmulated, Speech_StreamPos_RealTime, SWTAdded,
    DISPID_SRSetPropertyString, SSSPTRelativeToEnd,
    SPSMF_SAPI_PROPERTIES, SPEI_MAX_TTS,
    __MIDL___MIDL_itf_sapi_0000_0020_0002, SREStateChange,
    DISPID_SRCERequestUI, SPSHORTCUTPAIR, DISPID_SWFEBlockAlign,
    DISPID_SWFEBitsPerSample, SAFT16kHz16BitStereo,
    SpObjectTokenCategory, SRERecoOtherContext, DISPID_SLPSymbolic,
    DISPID_SPIGetText, DISPID_SOTGetStorageFileName,
    SAFT24kHz16BitStereo, ISpEventSource, DISPID_SVSLastBookmark,
    eLEXTYPE_PRIVATE11, DISPID_SPIGetDisplayAttributes,
    DISPID_SVGetAudioInputs, SVP_2, SAFTADPCM_8kHzMono,
    ISpeechRecoResultTimes, SAFTCCITT_ALaw_44kHzStereo,
    DISPID_SPRulesCount, DISPID_SOTCGetDataKey, SPSSuppressWord,
    DISPID_SAEventHandle, SGRSTTWord, eLEXTYPE_PRIVATE16,
    DISPID_SLGetWords, DISPID_SRAllowAudioInputFormatChangesOnNextSet,
    _RemotableHandle, SpeechCategoryRecognizers, SVSFParseSapi,
    SPSHT_Unknown, _lcid, SWPUnknownWordPronounceable,
    DISPID_SRSNumberOfActiveRules, DISPID_SOTDataKey, SP_VISEME_8,
    SVF_Emphasis, ISpAudio, SINoSignal, SpInprocRecognizer,
    DISPID_SVGetVoices, SpeechAddRemoveWord, DISPID_SRGetFormat,
    DISPID_SRCRecognizer, SPSFunction, SP_VISEME_9, SP_VISEME_3,
    DISPID_SAFSetWaveFormatEx, SDTDisplayText, DISPID_SGRSTransitions,
    SREAllEvents, DISPID_SPARecoResult, ISpNotifyTranslator, SVP_0,
    SpeechPropertyNormalConfidenceThreshold,
    DISPID_SRGCmdLoadFromResource, SREPhraseStart, DISPID_SRCPause,
    DISPID_SPRuleNumberOfElements, ISpeechTextSelectionInformation,
    SPRST_ACTIVE, SpeechPropertyComplexResponseSpeed,
    eLEXTYPE_RESERVED8, DISPID_SPAs_NewEnum, SAFTExtendedAudioFormat,
    DISPID_SAStatus, SpNotifyTranslator, SP_VISEME_0, SPPS_Verb,
    SpeechVoiceCategoryTTSRate, DISPID_SPRText, SVSFlagsAsync,
    SVF_None, SECNormalConfidence, eLEXTYPE_PRIVATE7, SGRSTTEpsilon,
    SDKLCurrentConfig, SVP_19, DISPID_SRGetPropertyString,
    DISPID_SRCEHypothesis, DISPID_SPEs_NewEnum,
    SpeechAudioFormatGUIDText, SpeechVoiceSkipTypeSentence,
    DISPID_SRRTimes, DISPID_SVSInputSentenceLength,
    DISPID_SGRsFindRule, DISPID_SLWPronunciations,
    DISPID_SPRuleEngineConfidence, DISPID_SMSSetData, SVSFIsNotXML,
    SPPS_RESERVED1, DISPID_SRState, ISpeechRecoResultDispatch,
    ISpeechRecognizerStatus, DISPID_SRRecognizer,
    SAFTGSM610_44kHzMono, DISPID_SLWLangId, SVP_11,
    SPWT_LEXICAL_NO_SPECIAL_CHARS, DISPID_SVEventInterests,
    DISPID_SPIEnginePrivateData, SPEI_MIN_SR, SPWF_SRENGINE,
    SpUnCompressedLexicon, SPINTERFERENCE_LATENCY_WARNING,
    SpeechCategoryRecoProfiles, SPCT_SUB_DICTATION,
    DISPID_SVDisplayUI, DISPID_SVEStreamStart, SpWaveFormatEx,
    SLTUser, SPEI_TTS_BOOKMARK, SpAudioFormat, SPEI_WORD_BOUNDARY,
    ISpeechGrammarRule, SGSExclusive, DISPID_SPPValue, SPFM_CREATE,
    typelib_path, SECFIgnoreCase, SVEPrivate,
    DISPID_SVSInputWordLength, DISPID_SPRulesItem, eLEXTYPE_PRIVATE1,
    SPEI_SOUND_END, SP_VISEME_18, DISPID_SABufferInfo, SPBO_NONE,
    SPEI_TTS_PRIVATE, DISPID_SMSADeviceId, SINone, DISPID_SGRSTWeight,
    DISPID_SOTCategory, SVPAlert, SVPOver, DISPID_SPACommit,
    SGLexical, DISPID_SOTIsUISupported, DISPID_SBSWrite,
    DISPID_SGRInitialState, SPEI_TTS_AUDIO_LEVEL,
    DISPID_SRCCreateGrammar, SLOStatic, SAFT48kHz16BitStereo, SPSVerb,
    eLEXTYPE_PRIVATE15, DISPID_SLAddPronunciationByPhoneIds,
    DISPID_SVSPhonemeId, DISPID_SGRSTPropertyValue, SASClosed,
    SRAInterpreter, SAFTADPCM_44kHzMono, eLEXTYPE_RESERVED7,
    ISpeechMemoryStream, SPPHRASEELEMENT, DISPID_SRCVoicePurgeEvent,
    SPPS_Noncontent, SPEI_FALSE_RECOGNITION, DISPID_SPEsCount,
    SpPhoneConverter, DISPID_SDKDeleteKey, SpeechUserTraining,
    SPLO_DYNAMIC, DISPID_SGRSAddSpecialTransition, DISPID_SRCBookmark,
    SPBO_PAUSE, DISPID_SFSOpen, SASRun, eLEXTYPE_RESERVED6,
    SVESentenceBoundary, SPWP_KNOWN_WORD_PRONOUNCEABLE,
    SPDKL_CurrentUser, DISPID_SPEActualConfidence, SPRECORESULTTIMES,
    DISPID_SLPPhoneIds, ISpeechXMLRecoResult, DISPID_SRCEPhraseStart,
    ISpGrammarBuilder, SASStop, DISPID_SLGetGenerationChange,
    SRTExtendableParse, DISPID_SGRClear, DISPID_SOTGetDescription,
    SSTTDictation, SPGS_ENABLED, Speech_Default_Weight, SITooQuiet,
    DISPID_SPEsItem, DISPID_SRCEEnginePrivate, DISPID_SOTCSetId,
    SECHighConfidence, SPWORD, SVSFUnusedFlags,
    DISPID_SVEEnginePrivate, IEnumSpObjectTokens, SpCompressedLexicon,
    DISPID_SAFGetWaveFormatEx, SPEI_ADAPTATION, SPTEXTSELECTIONINFO,
    DISPID_SLPsItem, SVP_4, DISPID_SWFESamplesPerSec, DISPID_SVStatus,
    SAFT11kHz8BitStereo, SPEI_PHRASE_START,
    DISPID_SRSCurrentStreamNumber, SPAO_RETAIN_AUDIO,
    DISPID_SDKCreateKey, SPSNoun, SPEI_RESERVED6, SRERecognition,
    DISPID_SRIsShared, ISpeechPhraseReplacement,
    DISPID_SRCAudioInInterferenceStatus, SpeechTokenIdUserLexicon,
    DISPID_SASFreeBufferSpace, SFTInput, SLTApp, ISpRecoCategory,
    SSSPTRelativeToCurrentPosition, SpStreamFormatConverter,
    SP_VISEME_14, SVP_15, DISPID_SRStatus, SAFT22kHz16BitStereo,
    DISPID_SGRsItem, SAFT8kHz16BitStereo, SPGS_DISABLED,
    ISpeechRecoResult, ISpeechDataKey, SRCS_Disabled,
    DISPID_SCSBaseStream, DISPID_SDKGetStringValue,
    SAFT22kHz8BitStereo, DISPID_SRRAudioFormat,
    DISPID_SRCRetainedAudioFormat, DISPID_SDKEnumKeys, SPAR_Unknown,
    DISPID_SPRuleName, DISPID_SRAudioInput, SAFT44kHz8BitStereo,
    SPPS_RESERVED3, SAFT22kHz8BitMono,
    SPSMF_SRGS_SEMANTICINTERPRETATION_W3C, DISPID_SGRAddResource,
    SPEI_MAX_SR, SAFTText, IServiceProvider, eLEXTYPE_PRIVATE17,
    eLEXTYPE_PRIVATE9, SPPS_Function, SREStreamStart, SpObjectToken,
    ISpeechPhoneConverter, DISPID_SGRSTRule, DISPID_SRIsUISupported,
    SVSFNLPSpeakPunc, SFTSREngine, SPVOICESTATUS,
    SpeechRegistryUserRoot, SpeechPropertyResponseSpeed,
    DISPID_SRCVoice, eLEXTYPE_LETTERTOSOUND, DISPID_SOTs_NewEnum,
    DISPID_SPRuleFirstElement, SDKLDefaultLocation, SpeechAllElements,
    SDTProperty, DISPID_SVSLastStreamNumberQueued,
    DISPID_SRGIsPronounceable, SAFT48kHz8BitStereo,
    DISPID_SRSCurrentStreamPosition, eLEXTYPE_RESERVED4,
    DISPID_SRCEFalseRecognition, DISPID_SRRGetXMLErrorInfo,
    ISpeechPhraseAlternate, eLEXTYPE_PRIVATE8, DISPID_SOTRemove,
    ISpeechPhraseAlternates, SpTextSelectionInformation,
    SAFTCCITT_uLaw_11kHzStereo, DISPID_SRGCommit,
    DISPID_SRCEEndStream, ISpRecognizer2, ISpStreamFormat,
    DISPID_SOTCreateInstance, DISPID_SOTDisplayUI, _LARGE_INTEGER,
    SPSHT_OTHER, DISPID_SVIsUISupported, ISpPhoneConverter,
    DISPID_SRRSaveToMemory, DISPID_SOTsCount, DISPID_SDKGetlongValue,
    SAFTCCITT_uLaw_22kHzMono, SPFM_OPEN_READWRITE,
    DISPID_SOTCEnumerateTokens, SITooSlow, ULONG_PTR,
    DISPID_SVSCurrentStreamNumber, VARIANT, eLEXTYPE_PRIVATE20,
    DISPID_SLRemovePronunciationByPhoneIds, DISPID_SVEVoiceChange,
    SP_VISEME_6, SPINTERFERENCE_TOOSLOW, SAFTCCITT_uLaw_11kHzMono,
    SVP_12, SP_VISEME_11, SAFT32kHz16BitMono, SECFEmulateResult,
    SAFT48kHz16BitMono, DISPID_SPRules_NewEnum, SPEI_RESERVED3,
    DISPID_SGRsCommitAndSave, DISPID_SGRsDynamic, SPWF_INPUT,
    SGRSTTTextBuffer, DISPID_SRGetPropertyNumber,
    DISPID_SABufferNotifySize, SREPropertyStringChange, SVPNormal,
    SAFT24kHz8BitStereo, DISPID_SVSInputWordPosition, SPRS_INACTIVE,
    DISPID_SVPriority, ISpeechObjectToken, SPDKL_CurrentConfig,
    DISPID_SRDisplayUI, SpeechCategoryAudioIn, SRADynamic,
    SDTLexicalForm, DISPID_SDKEnumValues, SGRSTTRule, SPEI_PHONEME,
    DISPID_SPIRule, IStream, BSTR, eLEXTYPE_PRIVATE12, SP_VISEME_16,
    SpResourceManager, SpeechTokenKeyUI, SP_VISEME_19,
    SVSFParseAutodetect, VARIANT_BOOL, DISPID_SGRId, DISPID_SGRSTType,
    DISPID_SRGCmdLoadFromMemory, SPAS_PAUSE, SBOPause,
    DISPID_SRRTOffsetFromStart, ISpeechBaseStream,
    SAFTCCITT_ALaw_44kHzMono, SRERequestUI,
    DISPID_SPEDisplayAttributes, ISpeechCustomStream, eLEXTYPE_USER,
    DISPID_SLPLangId, SPGS_EXCLUSIVE, SPWT_PRONUNCIATION, SPAR_High,
    SAFT44kHz8BitMono, DISPID_SVESentenceBoundary, ISpeechRecoContext,
    SpStream, SAFT32kHz16BitStereo, SPWORDPRONUNCIATIONLIST, SVP_9,
    SAFT32kHz8BitStereo, SAFT16kHz8BitStereo, ISpeechRecoResult2,
    DISPIDSPTSI_SelectionOffset, DISPID_SAFType, SRTAutopause,
    SVEViseme, DISPID_SRGSetWordSequenceData, SDTAlternates,
    eLEXTYPE_VENDORLEXICON, DISPID_SABIMinNotification, SpMMAudioOut,
    eLEXTYPE_PRIVATE5, SAFTADPCM_11kHzMono, DISPID_SVEViseme, WSTRING,
    SRARoot, SVP_14, DISPID_SDKSetStringValue, SGPronounciation,
    SVEAudioLevel, SpeechGrammarTagWildcard, ISpProperties,
    tagSTATSTG, SVSFPurgeBeforeSpeak, SSFMOpenReadWrite,
    ISpeechGrammarRuleStateTransitions, SAFTNoAssignedFormat, STCAll,
    DISPID_SRCEStartStream, SPEI_UNDEFINED, _ISpeechRecoContextEvents,
    SPSHT_NotOverriden, DISPID_SRCCmdMaxAlternates,
    ISpeechPhraseElements, SPEI_ACTIVE_CATEGORY_CHANGED,
    DISPID_SRGRules, DISPID_SPPBRestorePhraseFromMemory,
    SPBINARYGRAMMAR, DISPID_SGRSTPropertyId, SPRECOCONTEXTSTATUS,
    SPSMF_SRGS_SEMANTICINTERPRETATION_MS,
    SpeechPropertyHighConfidenceThreshold, SP_VISEME_7,
    SAFT32kHz8BitMono, DISPID_SLAddPronunciation,
    SPXRO_Alternates_SML, SSTTWildcard, DISPID_SRGDictationUnload,
    DISPID_SRCESoundStart, helpstring, DISPID_SLGetPronunciations,
    SpeechEngineProperties, DISPID_SASetState,
    SAFTCCITT_uLaw_44kHzMono, DISPID_SRCEventInterests,
    SpMemoryStream, SPCT_COMMAND, Speech_Max_Word_Length,
    DISPID_SRRTTickCount, DISPID_SPPName, SpeechTokenKeyAttributes,
    SPPS_NotOverriden, SpeechDictationTopicSpelling,
    DISPID_SGRSTNextState, DISPID_SLPPartOfSpeech,
    DISPID_SWFEAvgBytesPerSec, SpSharedRecognizer,
    DISPID_SRRTStreamTime, DISPID_SVWaitUntilDone, DISPID_SOTsItem,
    DISPID_SDKSetBinaryValue, DISPID_SOTId, DISPID_SGRSTPropertyName,
    SpNullPhoneConverter, SREPropertyNumChange, DISPID_SAVolume,
    ISpRecoResult, ISpStreamFormatConverter, DISPID_SRCResume,
    SAFTADPCM_22kHzMono, DISPID_SLPType, DISPID_SABIBufferSize,
    ISpeechObjectTokens, SRAORetainAudio, SGDSActiveUserDelimited,
    SPVPRI_ALERT, SVSFNLPMask, DISPID_SDKSetLongValue, SVF_Stressed,
    DISPID_SRRSetTextFeedback, SRADefaultToActive,
    SPEI_SENTENCE_BOUNDARY, DISPID_SOTGetAttribute,
    DISPID_SLPs_NewEnum, DISPID_SLPsCount, ISpeechRecoGrammar,
    SRSEIsSpeaking, SAFTCCITT_ALaw_8kHzStereo,
    SAFTCCITT_uLaw_8kHzStereo, DISPID_SPRNumberOfElements,
    DISPID_SMSALineId, SAFTGSM610_8kHzMono
)


class SpeechStreamSeekPositionType(IntFlag):
    SSSPTRelativeToStart = 0
    SSSPTRelativeToCurrentPosition = 1
    SSSPTRelativeToEnd = 2


class SpeechStreamFileMode(IntFlag):
    SSFMOpenForRead = 0
    SSFMOpenReadWrite = 1
    SSFMCreate = 2
    SSFMCreateForWrite = 3


class SpeechAudioState(IntFlag):
    SASClosed = 0
    SASStop = 1
    SASPause = 2
    SASRun = 3


class SpeechAudioFormatType(IntFlag):
    SAFTDefault = -1
    SAFTNoAssignedFormat = 0
    SAFTText = 1
    SAFTNonStandardFormat = 2
    SAFTExtendedAudioFormat = 3
    SAFT8kHz8BitMono = 4
    SAFT8kHz8BitStereo = 5
    SAFT8kHz16BitMono = 6
    SAFT8kHz16BitStereo = 7
    SAFT11kHz8BitMono = 8
    SAFT11kHz8BitStereo = 9
    SAFT11kHz16BitMono = 10
    SAFT11kHz16BitStereo = 11
    SAFT12kHz8BitMono = 12
    SAFT12kHz8BitStereo = 13
    SAFT12kHz16BitMono = 14
    SAFT12kHz16BitStereo = 15
    SAFT16kHz8BitMono = 16
    SAFT16kHz8BitStereo = 17
    SAFT16kHz16BitMono = 18
    SAFT16kHz16BitStereo = 19
    SAFT22kHz8BitMono = 20
    SAFT22kHz8BitStereo = 21
    SAFT22kHz16BitMono = 22
    SAFT22kHz16BitStereo = 23
    SAFT24kHz8BitMono = 24
    SAFT24kHz8BitStereo = 25
    SAFT24kHz16BitMono = 26
    SAFT24kHz16BitStereo = 27
    SAFT32kHz8BitMono = 28
    SAFT32kHz8BitStereo = 29
    SAFT32kHz16BitMono = 30
    SAFT32kHz16BitStereo = 31
    SAFT44kHz8BitMono = 32
    SAFT44kHz8BitStereo = 33
    SAFT44kHz16BitMono = 34
    SAFT44kHz16BitStereo = 35
    SAFT48kHz8BitMono = 36
    SAFT48kHz8BitStereo = 37
    SAFT48kHz16BitMono = 38
    SAFT48kHz16BitStereo = 39
    SAFTTrueSpeech_8kHz1BitMono = 40
    SAFTCCITT_ALaw_8kHzMono = 41
    SAFTCCITT_ALaw_8kHzStereo = 42
    SAFTCCITT_ALaw_11kHzMono = 43
    SAFTCCITT_ALaw_11kHzStereo = 44
    SAFTCCITT_ALaw_22kHzMono = 45
    SAFTCCITT_ALaw_22kHzStereo = 46
    SAFTCCITT_ALaw_44kHzMono = 47
    SAFTCCITT_ALaw_44kHzStereo = 48
    SAFTCCITT_uLaw_8kHzMono = 49
    SAFTCCITT_uLaw_8kHzStereo = 50
    SAFTCCITT_uLaw_11kHzMono = 51
    SAFTCCITT_uLaw_11kHzStereo = 52
    SAFTCCITT_uLaw_22kHzMono = 53
    SAFTCCITT_uLaw_22kHzStereo = 54
    SAFTCCITT_uLaw_44kHzMono = 55
    SAFTCCITT_uLaw_44kHzStereo = 56
    SAFTADPCM_8kHzMono = 57
    SAFTADPCM_8kHzStereo = 58
    SAFTADPCM_11kHzMono = 59
    SAFTADPCM_11kHzStereo = 60
    SAFTADPCM_22kHzMono = 61
    SAFTADPCM_22kHzStereo = 62
    SAFTADPCM_44kHzMono = 63
    SAFTADPCM_44kHzStereo = 64
    SAFTGSM610_8kHzMono = 65
    SAFTGSM610_11kHzMono = 66
    SAFTGSM610_22kHzMono = 67
    SAFTGSM610_44kHzMono = 68


class _SPAUDIOSTATE(IntFlag):
    SPAS_CLOSED = 0
    SPAS_STOP = 1
    SPAS_PAUSE = 2
    SPAS_RUN = 3


class SpeechVoiceEvents(IntFlag):
    SVEStartInputStream = 2
    SVEEndInputStream = 4
    SVEVoiceChange = 8
    SVEBookmark = 16
    SVEWordBoundary = 32
    SVEPhoneme = 64
    SVESentenceBoundary = 128
    SVEViseme = 256
    SVEAudioLevel = 512
    SVEPrivate = 32768
    SVEAllEvents = 33790


class SpeechVoicePriority(IntFlag):
    SVPNormal = 0
    SVPAlert = 1
    SVPOver = 2


class SpeechVoiceSpeakFlags(IntFlag):
    SVSFDefault = 0
    SVSFlagsAsync = 1
    SVSFPurgeBeforeSpeak = 2
    SVSFIsFilename = 4
    SVSFIsXML = 8
    SVSFIsNotXML = 16
    SVSFPersistXML = 32
    SVSFNLPSpeakPunc = 64
    SVSFParseSapi = 128
    SVSFParseSsml = 256
    SVSFParseAutodetect = 0
    SVSFNLPMask = 64
    SVSFParseMask = 384
    SVSFVoiceMask = 511
    SVSFUnusedFlags = -512


class SpeechRuleAttributes(IntFlag):
    SRATopLevel = 1
    SRADefaultToActive = 2
    SRAExport = 4
    SRAImport = 8
    SRAInterpreter = 16
    SRADynamic = 32
    SRARoot = 64


class SpeechGrammarWordType(IntFlag):
    SGDisplay = 0
    SGLexical = 1
    SGPronounciation = 2
    SGLexicalNoSpecialChars = 3


class SpeechSpecialTransitionType(IntFlag):
    SSTTWildcard = 1
    SSTTDictation = 2
    SSTTTextBuffer = 3


class SpeechInterference(IntFlag):
    SINone = 0
    SINoise = 1
    SINoSignal = 2
    SITooLoud = 3
    SITooQuiet = 4
    SITooFast = 5
    SITooSlow = 6


class SPWAVEFORMATTYPE(IntFlag):
    SPWF_INPUT = 0
    SPWF_SRENGINE = 1


class SpeechGrammarRuleStateTransitionType(IntFlag):
    SGRSTTEpsilon = 0
    SGRSTTWord = 1
    SGRSTTRule = 2
    SGRSTTDictation = 3
    SGRSTTWildcard = 4
    SGRSTTTextBuffer = 5


class SpeechDiscardType(IntFlag):
    SDTProperty = 1
    SDTReplacement = 2
    SDTRule = 4
    SDTDisplayText = 8
    SDTLexicalForm = 16
    SDTPronunciation = 32
    SDTAudio = 64
    SDTAlternates = 128
    SDTAll = 255


class SpeechDisplayAttributes(IntFlag):
    SDA_No_Trailing_Space = 0
    SDA_One_Trailing_Space = 2
    SDA_Two_Trailing_Spaces = 4
    SDA_Consume_Leading_Spaces = 8


class SpeechVisemeType(IntFlag):
    SVP_0 = 0
    SVP_1 = 1
    SVP_2 = 2
    SVP_3 = 3
    SVP_4 = 4
    SVP_5 = 5
    SVP_6 = 6
    SVP_7 = 7
    SVP_8 = 8
    SVP_9 = 9
    SVP_10 = 10
    SVP_11 = 11
    SVP_12 = 12
    SVP_13 = 13
    SVP_14 = 14
    SVP_15 = 15
    SVP_16 = 16
    SVP_17 = 17
    SVP_18 = 18
    SVP_19 = 19
    SVP_20 = 20
    SVP_21 = 21


class SpeechEngineConfidence(IntFlag):
    SECLowConfidence = -1
    SECNormalConfidence = 0
    SECHighConfidence = 1


class SPSEMANTICFORMAT(IntFlag):
    SPSMF_SAPI_PROPERTIES = 0
    SPSMF_SRGS_SEMANTICINTERPRETATION_MS = 1
    SPSMF_SRGS_SAPIPROPERTIES = 2
    SPSMF_UPS = 4
    SPSMF_SRGS_SEMANTICINTERPRETATION_W3C = 8


class SpeechRecognizerState(IntFlag):
    SRSInactive = 0
    SRSActive = 1
    SRSActiveAlways = 2
    SRSInactiveWithPurge = 3


class SpeechLexiconType(IntFlag):
    SLTUser = 1
    SLTApp = 2


class SpeechPartOfSpeech(IntFlag):
    SPSNotOverriden = -1
    SPSUnknown = 0
    SPSNoun = 4096
    SPSVerb = 8192
    SPSModifier = 12288
    SPSFunction = 16384
    SPSInterjection = 20480
    SPSLMA = 28672
    SPSSuppressWord = 61440


class SPVISEMES(IntFlag):
    SP_VISEME_0 = 0
    SP_VISEME_1 = 1
    SP_VISEME_2 = 2
    SP_VISEME_3 = 3
    SP_VISEME_4 = 4
    SP_VISEME_5 = 5
    SP_VISEME_6 = 6
    SP_VISEME_7 = 7
    SP_VISEME_8 = 8
    SP_VISEME_9 = 9
    SP_VISEME_10 = 10
    SP_VISEME_11 = 11
    SP_VISEME_12 = 12
    SP_VISEME_13 = 13
    SP_VISEME_14 = 14
    SP_VISEME_15 = 15
    SP_VISEME_16 = 16
    SP_VISEME_17 = 17
    SP_VISEME_18 = 18
    SP_VISEME_19 = 19
    SP_VISEME_20 = 20
    SP_VISEME_21 = 21


class SpeechWordType(IntFlag):
    SWTAdded = 1
    SWTDeleted = 2


class SPGRAMMARWORDTYPE(IntFlag):
    SPWT_DISPLAY = 0
    SPWT_LEXICAL = 1
    SPWT_PRONUNCIATION = 2
    SPWT_LEXICAL_NO_SPECIAL_CHARS = 3


class SPLOADOPTIONS(IntFlag):
    SPLO_STATIC = 0
    SPLO_DYNAMIC = 1


class SPXMLRESULTOPTIONS(IntFlag):
    SPXRO_SML = 0
    SPXRO_Alternates_SML = 1


class SPRULESTATE(IntFlag):
    SPRS_INACTIVE = 0
    SPRS_ACTIVE = 1
    SPRS_ACTIVE_WITH_AUTO_PAUSE = 3
    SPRS_ACTIVE_USER_DELIMITED = 4


class SPWORDPRONOUNCEABLE(IntFlag):
    SPWP_UNKNOWN_WORD_UNPRONOUNCEABLE = 0
    SPWP_UNKNOWN_WORD_PRONOUNCEABLE = 1
    SPWP_KNOWN_WORD_PRONOUNCEABLE = 2


class SPGRAMMARSTATE(IntFlag):
    SPGS_DISABLED = 0
    SPGS_ENABLED = 1
    SPGS_EXCLUSIVE = 3


class SPINTERFERENCE(IntFlag):
    SPINTERFERENCE_NONE = 0
    SPINTERFERENCE_NOISE = 1
    SPINTERFERENCE_NOSIGNAL = 2
    SPINTERFERENCE_TOOLOUD = 3
    SPINTERFERENCE_TOOQUIET = 4
    SPINTERFERENCE_TOOFAST = 5
    SPINTERFERENCE_TOOSLOW = 6
    SPINTERFERENCE_LATENCY_WARNING = 7
    SPINTERFERENCE_LATENCY_TRUNCATE_BEGIN = 8
    SPINTERFERENCE_LATENCY_TRUNCATE_END = 9


class SPAUDIOOPTIONS(IntFlag):
    SPAO_NONE = 0
    SPAO_RETAIN_AUDIO = 1


class SPDATAKEYLOCATION(IntFlag):
    SPDKL_DefaultLocation = 0
    SPDKL_CurrentUser = 1
    SPDKL_LocalMachine = 2
    SPDKL_CurrentConfig = 5


class SPBOOKMARKOPTIONS(IntFlag):
    SPBO_NONE = 0
    SPBO_PAUSE = 1
    SPBO_AHEAD = 2
    SPBO_TIME_UNITS = 4


class SPCONTEXTSTATE(IntFlag):
    SPCS_DISABLED = 0
    SPCS_ENABLED = 1


class SPADAPTATIONRELEVANCE(IntFlag):
    SPAR_Unknown = 0
    SPAR_Low = 1
    SPAR_Medium = 2
    SPAR_High = 3


class SPCATEGORYTYPE(IntFlag):
    SPCT_COMMAND = 0
    SPCT_DICTATION = 1
    SPCT_SLEEP = 2
    SPCT_SUB_COMMAND = 3
    SPCT_SUB_DICTATION = 4


class SPLEXICONTYPE(IntFlag):
    eLEXTYPE_USER = 1
    eLEXTYPE_APP = 2
    eLEXTYPE_VENDORLEXICON = 4
    eLEXTYPE_LETTERTOSOUND = 8
    eLEXTYPE_MORPHOLOGY = 16
    eLEXTYPE_RESERVED4 = 32
    eLEXTYPE_USER_SHORTCUT = 64
    eLEXTYPE_RESERVED6 = 128
    eLEXTYPE_RESERVED7 = 256
    eLEXTYPE_RESERVED8 = 512
    eLEXTYPE_RESERVED9 = 1024
    eLEXTYPE_RESERVED10 = 2048
    eLEXTYPE_PRIVATE1 = 4096
    eLEXTYPE_PRIVATE2 = 8192
    eLEXTYPE_PRIVATE3 = 16384
    eLEXTYPE_PRIVATE4 = 32768
    eLEXTYPE_PRIVATE5 = 65536
    eLEXTYPE_PRIVATE6 = 131072
    eLEXTYPE_PRIVATE7 = 262144
    eLEXTYPE_PRIVATE8 = 524288
    eLEXTYPE_PRIVATE9 = 1048576
    eLEXTYPE_PRIVATE10 = 2097152
    eLEXTYPE_PRIVATE11 = 4194304
    eLEXTYPE_PRIVATE12 = 8388608
    eLEXTYPE_PRIVATE13 = 16777216
    eLEXTYPE_PRIVATE14 = 33554432
    eLEXTYPE_PRIVATE15 = 67108864
    eLEXTYPE_PRIVATE16 = 134217728
    eLEXTYPE_PRIVATE17 = 268435456
    eLEXTYPE_PRIVATE18 = 536870912
    eLEXTYPE_PRIVATE19 = 1073741824
    eLEXTYPE_PRIVATE20 = -2147483648


class SPPARTOFSPEECH(IntFlag):
    SPPS_NotOverriden = -1
    SPPS_Unknown = 0
    SPPS_Noun = 4096
    SPPS_Verb = 8192
    SPPS_Modifier = 12288
    SPPS_Function = 16384
    SPPS_Interjection = 20480
    SPPS_Noncontent = 24576
    SPPS_LMA = 28672
    SPPS_SuppressWord = 61440


class SPWORDTYPE(IntFlag):
    eWORDTYPE_ADDED = 1
    eWORDTYPE_DELETED = 2


class SPSHORTCUTTYPE(IntFlag):
    SPSHT_NotOverriden = -1
    SPSHT_Unknown = 0
    SPSHT_EMAIL = 4096
    SPSHT_OTHER = 8192
    SPPS_RESERVED1 = 12288
    SPPS_RESERVED2 = 16384
    SPPS_RESERVED3 = 20480
    SPPS_RESERVED4 = 61440


class SpeechTokenContext(IntFlag):
    STCInprocServer = 1
    STCInprocHandler = 2
    STCLocalServer = 4
    STCRemoteServer = 16
    STCAll = 23


class SpeechTokenShellFolder(IntFlag):
    STSF_AppData = 26
    STSF_LocalAppData = 28
    STSF_CommonAppData = 35
    STSF_FlagCreate = 32768


class SpeechVisemeFeature(IntFlag):
    SVF_None = 0
    SVF_Stressed = 1
    SVF_Emphasis = 2


class SpeechDataKeyLocation(IntFlag):
    SDKLDefaultLocation = 0
    SDKLCurrentUser = 1
    SDKLLocalMachine = 2
    SDKLCurrentConfig = 5


class DISPID_SpeechDataKey(IntFlag):
    DISPID_SDKSetBinaryValue = 1
    DISPID_SDKGetBinaryValue = 2
    DISPID_SDKSetStringValue = 3
    DISPID_SDKGetStringValue = 4
    DISPID_SDKSetLongValue = 5
    DISPID_SDKGetlongValue = 6
    DISPID_SDKOpenKey = 7
    DISPID_SDKCreateKey = 8
    DISPID_SDKDeleteKey = 9
    DISPID_SDKDeleteValue = 10
    DISPID_SDKEnumKeys = 11
    DISPID_SDKEnumValues = 12


class DISPID_SpeechObjectToken(IntFlag):
    DISPID_SOTId = 1
    DISPID_SOTDataKey = 2
    DISPID_SOTCategory = 3
    DISPID_SOTGetDescription = 4
    DISPID_SOTSetId = 5
    DISPID_SOTGetAttribute = 6
    DISPID_SOTCreateInstance = 7
    DISPID_SOTRemove = 8
    DISPID_SOTGetStorageFileName = 9
    DISPID_SOTRemoveStorageFileName = 10
    DISPID_SOTIsUISupported = 11
    DISPID_SOTDisplayUI = 12
    DISPID_SOTMatchesAttributes = 13


class DISPID_SpeechObjectTokens(IntFlag):
    DISPID_SOTsCount = 1
    DISPID_SOTsItem = 0
    DISPID_SOTs_NewEnum = -4


class SpeechRunState(IntFlag):
    SRSEDone = 1
    SRSEIsSpeaking = 2


class DISPID_SpeechObjectTokenCategory(IntFlag):
    DISPID_SOTCId = 1
    DISPID_SOTCDefault = 2
    DISPID_SOTCSetId = 3
    DISPID_SOTCGetDataKey = 4
    DISPID_SOTCEnumerateTokens = 5


class SPFILEMODE(IntFlag):
    SPFM_OPEN_READONLY = 0
    SPFM_OPEN_READWRITE = 1
    SPFM_CREATE = 2
    SPFM_CREATE_ALWAYS = 3
    SPFM_NUM_MODES = 4


class DISPID_SpeechAudioFormat(IntFlag):
    DISPID_SAFType = 1
    DISPID_SAFGuid = 2
    DISPID_SAFGetWaveFormatEx = 3
    DISPID_SAFSetWaveFormatEx = 4


class DISPID_SpeechBaseStream(IntFlag):
    DISPID_SBSFormat = 1
    DISPID_SBSRead = 2
    DISPID_SBSWrite = 3
    DISPID_SBSSeek = 4


class DISPID_SpeechAudio(IntFlag):
    DISPID_SAStatus = 200
    DISPID_SABufferInfo = 201
    DISPID_SADefaultFormat = 202
    DISPID_SAVolume = 203
    DISPID_SABufferNotifySize = 204
    DISPID_SAEventHandle = 205
    DISPID_SASetState = 206


class DISPID_SpeechMMSysAudio(IntFlag):
    DISPID_SMSADeviceId = 300
    DISPID_SMSALineId = 301
    DISPID_SMSAMMHandle = 302


class DISPID_SpeechFileStream(IntFlag):
    DISPID_SFSOpen = 100
    DISPID_SFSClose = 101


class SPVPRIORITY(IntFlag):
    SPVPRI_NORMAL = 0
    SPVPRI_ALERT = 1
    SPVPRI_OVER = 2


class SPEVENTENUM(IntFlag):
    SPEI_UNDEFINED = 0
    SPEI_START_INPUT_STREAM = 1
    SPEI_END_INPUT_STREAM = 2
    SPEI_VOICE_CHANGE = 3
    SPEI_TTS_BOOKMARK = 4
    SPEI_WORD_BOUNDARY = 5
    SPEI_PHONEME = 6
    SPEI_SENTENCE_BOUNDARY = 7
    SPEI_VISEME = 8
    SPEI_TTS_AUDIO_LEVEL = 9
    SPEI_TTS_PRIVATE = 15
    SPEI_MIN_TTS = 1
    SPEI_MAX_TTS = 15
    SPEI_END_SR_STREAM = 34
    SPEI_SOUND_START = 35
    SPEI_SOUND_END = 36
    SPEI_PHRASE_START = 37
    SPEI_RECOGNITION = 38
    SPEI_HYPOTHESIS = 39
    SPEI_SR_BOOKMARK = 40
    SPEI_PROPERTY_NUM_CHANGE = 41
    SPEI_PROPERTY_STRING_CHANGE = 42
    SPEI_FALSE_RECOGNITION = 43
    SPEI_INTERFERENCE = 44
    SPEI_REQUEST_UI = 45
    SPEI_RECO_STATE_CHANGE = 46
    SPEI_ADAPTATION = 47
    SPEI_START_SR_STREAM = 48
    SPEI_RECO_OTHER_CONTEXT = 49
    SPEI_SR_AUDIO_LEVEL = 50
    SPEI_SR_RETAINEDAUDIO = 51
    SPEI_SR_PRIVATE = 52
    SPEI_ACTIVE_CATEGORY_CHANGED = 53
    SPEI_RESERVED5 = 54
    SPEI_RESERVED6 = 55
    SPEI_MIN_SR = 34
    SPEI_MAX_SR = 55
    SPEI_RESERVED1 = 30
    SPEI_RESERVED2 = 33
    SPEI_RESERVED3 = 63


class DISPID_SpeechCustomStream(IntFlag):
    DISPID_SCSBaseStream = 100


class DISPID_SpeechMemoryStream(IntFlag):
    DISPID_SMSSetData = 100
    DISPID_SMSGetData = 101


class DISPID_SpeechAudioStatus(IntFlag):
    DISPID_SASFreeBufferSpace = 1
    DISPID_SASNonBlockingIO = 2
    DISPID_SASState = 3
    DISPID_SASCurrentSeekPosition = 4
    DISPID_SASCurrentDevicePosition = 5


class SpeechLoadOption(IntFlag):
    SLOStatic = 0
    SLODynamic = 1


class DISPID_SpeechAudioBufferInfo(IntFlag):
    DISPID_SABIMinNotification = 1
    DISPID_SABIBufferSize = 2
    DISPID_SABIEventBias = 3


class DISPID_SpeechWaveFormatEx(IntFlag):
    DISPID_SWFEFormatTag = 1
    DISPID_SWFEChannels = 2
    DISPID_SWFESamplesPerSec = 3
    DISPID_SWFEAvgBytesPerSec = 4
    DISPID_SWFEBlockAlign = 5
    DISPID_SWFEBitsPerSample = 6
    DISPID_SWFEExtraData = 7


class DISPID_SpeechVoice(IntFlag):
    DISPID_SVStatus = 1
    DISPID_SVVoice = 2
    DISPID_SVAudioOutput = 3
    DISPID_SVAudioOutputStream = 4
    DISPID_SVRate = 5
    DISPID_SVVolume = 6
    DISPID_SVAllowAudioOuputFormatChangesOnNextSet = 7
    DISPID_SVEventInterests = 8
    DISPID_SVPriority = 9
    DISPID_SVAlertBoundary = 10
    DISPID_SVSyncronousSpeakTimeout = 11
    DISPID_SVSpeak = 12
    DISPID_SVSpeakStream = 13
    DISPID_SVPause = 14
    DISPID_SVResume = 15
    DISPID_SVSkip = 16
    DISPID_SVGetVoices = 17
    DISPID_SVGetAudioOutputs = 18
    DISPID_SVWaitUntilDone = 19
    DISPID_SVSpeakCompleteEvent = 20
    DISPID_SVIsUISupported = 21
    DISPID_SVDisplayUI = 22


class DISPID_SpeechVoiceStatus(IntFlag):
    DISPID_SVSCurrentStreamNumber = 1
    DISPID_SVSLastStreamNumberQueued = 2
    DISPID_SVSLastResult = 3
    DISPID_SVSRunningState = 4
    DISPID_SVSInputWordPosition = 5
    DISPID_SVSInputWordLength = 6
    DISPID_SVSInputSentencePosition = 7
    DISPID_SVSInputSentenceLength = 8
    DISPID_SVSLastBookmark = 9
    DISPID_SVSLastBookmarkId = 10
    DISPID_SVSPhonemeId = 11
    DISPID_SVSVisemeId = 12


class DISPID_SpeechVoiceEvent(IntFlag):
    DISPID_SVEStreamStart = 1
    DISPID_SVEStreamEnd = 2
    DISPID_SVEVoiceChange = 3
    DISPID_SVEBookmark = 4
    DISPID_SVEWord = 5
    DISPID_SVEPhoneme = 6
    DISPID_SVESentenceBoundary = 7
    DISPID_SVEViseme = 8
    DISPID_SVEAudioLevel = 9
    DISPID_SVEEnginePrivate = 10


class DISPID_SpeechRecognizer(IntFlag):
    DISPID_SRRecognizer = 1
    DISPID_SRAllowAudioInputFormatChangesOnNextSet = 2
    DISPID_SRAudioInput = 3
    DISPID_SRAudioInputStream = 4
    DISPID_SRIsShared = 5
    DISPID_SRState = 6
    DISPID_SRStatus = 7
    DISPID_SRProfile = 8
    DISPID_SREmulateRecognition = 9
    DISPID_SRCreateRecoContext = 10
    DISPID_SRGetFormat = 11
    DISPID_SRSetPropertyNumber = 12
    DISPID_SRGetPropertyNumber = 13
    DISPID_SRSetPropertyString = 14
    DISPID_SRGetPropertyString = 15
    DISPID_SRIsUISupported = 16
    DISPID_SRDisplayUI = 17
    DISPID_SRGetRecognizers = 18
    DISPID_SVGetAudioInputs = 19
    DISPID_SVGetProfiles = 20


class SpeechEmulationCompareFlags(IntFlag):
    SECFIgnoreCase = 1
    SECFIgnoreKanaType = 65536
    SECFIgnoreWidth = 131072
    SECFNoSpecialChars = 536870912
    SECFEmulateResult = 1073741824
    SECFDefault = 196609


class DISPID_SpeechRecognizerStatus(IntFlag):
    DISPID_SRSAudioStatus = 1
    DISPID_SRSCurrentStreamPosition = 2
    DISPID_SRSCurrentStreamNumber = 3
    DISPID_SRSNumberOfActiveRules = 4
    DISPID_SRSClsidEngine = 5
    DISPID_SRSSupportedLanguages = 6


class SPRECOSTATE(IntFlag):
    SPRST_INACTIVE = 0
    SPRST_ACTIVE = 1
    SPRST_ACTIVE_ALWAYS = 2
    SPRST_INACTIVE_WITH_PURGE = 3
    SPRST_NUM_STATES = 4


class DISPID_SpeechRecoContext(IntFlag):
    DISPID_SRCRecognizer = 1
    DISPID_SRCAudioInInterferenceStatus = 2
    DISPID_SRCRequestedUIType = 3
    DISPID_SRCVoice = 4
    DISPID_SRAllowVoiceFormatMatchingOnNextSet = 5
    DISPID_SRCVoicePurgeEvent = 6
    DISPID_SRCEventInterests = 7
    DISPID_SRCCmdMaxAlternates = 8
    DISPID_SRCState = 9
    DISPID_SRCRetainedAudio = 10
    DISPID_SRCRetainedAudioFormat = 11
    DISPID_SRCPause = 12
    DISPID_SRCResume = 13
    DISPID_SRCCreateGrammar = 14
    DISPID_SRCCreateResultFromMemory = 15
    DISPID_SRCBookmark = 16
    DISPID_SRCSetAdaptationData = 17


class DISPIDSPRG(IntFlag):
    DISPID_SRGId = 1
    DISPID_SRGRecoContext = 2
    DISPID_SRGState = 3
    DISPID_SRGRules = 4
    DISPID_SRGReset = 5
    DISPID_SRGCommit = 6
    DISPID_SRGCmdLoadFromFile = 7
    DISPID_SRGCmdLoadFromObject = 8
    DISPID_SRGCmdLoadFromResource = 9
    DISPID_SRGCmdLoadFromMemory = 10
    DISPID_SRGCmdLoadFromProprietaryGrammar = 11
    DISPID_SRGCmdSetRuleState = 12
    DISPID_SRGCmdSetRuleIdState = 13
    DISPID_SRGDictationLoad = 14
    DISPID_SRGDictationUnload = 15
    DISPID_SRGDictationSetState = 16
    DISPID_SRGSetWordSequenceData = 17
    DISPID_SRGSetTextSelection = 18
    DISPID_SRGIsPronounceable = 19


class DISPID_SpeechRecoContextEvents(IntFlag):
    DISPID_SRCEStartStream = 1
    DISPID_SRCEEndStream = 2
    DISPID_SRCEBookmark = 3
    DISPID_SRCESoundStart = 4
    DISPID_SRCESoundEnd = 5
    DISPID_SRCEPhraseStart = 6
    DISPID_SRCERecognition = 7
    DISPID_SRCEHypothesis = 8
    DISPID_SRCEPropertyNumberChange = 9
    DISPID_SRCEPropertyStringChange = 10
    DISPID_SRCEFalseRecognition = 11
    DISPID_SRCEInterference = 12
    DISPID_SRCERequestUI = 13
    DISPID_SRCERecognizerStateChange = 14
    DISPID_SRCEAdaptation = 15
    DISPID_SRCERecognitionForOtherContext = 16
    DISPID_SRCEAudioLevel = 17
    DISPID_SRCEEnginePrivate = 18


class DISPID_SpeechGrammarRule(IntFlag):
    DISPID_SGRAttributes = 1
    DISPID_SGRInitialState = 2
    DISPID_SGRName = 3
    DISPID_SGRId = 4
    DISPID_SGRClear = 5
    DISPID_SGRAddResource = 6
    DISPID_SGRAddState = 7


class SpeechBookmarkOptions(IntFlag):
    SBONone = 0
    SBOPause = 1


class SpeechRecognitionType(IntFlag):
    SRTStandard = 0
    SRTAutopause = 1
    SRTEmulated = 2
    SRTSMLTimeout = 4
    SRTExtendableParse = 8
    SRTReSent = 16


class DISPID_SpeechGrammarRules(IntFlag):
    DISPID_SGRsCount = 1
    DISPID_SGRsDynamic = 2
    DISPID_SGRsAdd = 3
    DISPID_SGRsCommit = 4
    DISPID_SGRsCommitAndSave = 5
    DISPID_SGRsFindRule = 6
    DISPID_SGRsItem = 0
    DISPID_SGRs_NewEnum = -4


class DISPID_SpeechGrammarRuleState(IntFlag):
    DISPID_SGRSRule = 1
    DISPID_SGRSTransitions = 2
    DISPID_SGRSAddWordTransition = 3
    DISPID_SGRSAddRuleTransition = 4
    DISPID_SGRSAddSpecialTransition = 5


class DISPID_SpeechGrammarRuleStateTransitions(IntFlag):
    DISPID_SGRSTsCount = 1
    DISPID_SGRSTsItem = 0
    DISPID_SGRSTs_NewEnum = -4


class DISPID_SpeechGrammarRuleStateTransition(IntFlag):
    DISPID_SGRSTType = 1
    DISPID_SGRSTText = 2
    DISPID_SGRSTRule = 3
    DISPID_SGRSTWeight = 4
    DISPID_SGRSTPropertyName = 5
    DISPID_SGRSTPropertyId = 6
    DISPID_SGRSTPropertyValue = 7
    DISPID_SGRSTNextState = 8


class DISPIDSPTSI(IntFlag):
    DISPIDSPTSI_ActiveOffset = 1
    DISPIDSPTSI_ActiveLength = 2
    DISPIDSPTSI_SelectionOffset = 3
    DISPIDSPTSI_SelectionLength = 4


class DISPID_SpeechRecoResult(IntFlag):
    DISPID_SRRRecoContext = 1
    DISPID_SRRTimes = 2
    DISPID_SRRAudioFormat = 3
    DISPID_SRRPhraseInfo = 4
    DISPID_SRRAlternates = 5
    DISPID_SRRAudio = 6
    DISPID_SRRSpeakAudio = 7
    DISPID_SRRSaveToMemory = 8
    DISPID_SRRDiscardResultInfo = 9


class DISPID_SpeechXMLRecoResult(IntFlag):
    DISPID_SRRGetXMLResult = 10
    DISPID_SRRGetXMLErrorInfo = 11


class DISPID_SpeechRecoResult2(IntFlag):
    DISPID_SRRSetTextFeedback = 12


class DISPID_SpeechPhraseBuilder(IntFlag):
    DISPID_SPPBRestorePhraseFromMemory = 1


class DISPID_SpeechRecoResultTimes(IntFlag):
    DISPID_SRRTStreamTime = 1
    DISPID_SRRTLength = 2
    DISPID_SRRTTickCount = 3
    DISPID_SRRTOffsetFromStart = 4


class DISPID_SpeechPhraseAlternate(IntFlag):
    DISPID_SPARecoResult = 1
    DISPID_SPAStartElementInResult = 2
    DISPID_SPANumberOfElementsInResult = 3
    DISPID_SPAPhraseInfo = 4
    DISPID_SPACommit = 5


class DISPID_SpeechPhraseAlternates(IntFlag):
    DISPID_SPAsCount = 1
    DISPID_SPAsItem = 0
    DISPID_SPAs_NewEnum = -4


class DISPID_SpeechPhraseInfo(IntFlag):
    DISPID_SPILanguageId = 1
    DISPID_SPIGrammarId = 2
    DISPID_SPIStartTime = 3
    DISPID_SPIAudioStreamPosition = 4
    DISPID_SPIAudioSizeBytes = 5
    DISPID_SPIRetainedSizeBytes = 6
    DISPID_SPIAudioSizeTime = 7
    DISPID_SPIRule = 8
    DISPID_SPIProperties = 9
    DISPID_SPIElements = 10
    DISPID_SPIReplacements = 11
    DISPID_SPIEngineId = 12
    DISPID_SPIEnginePrivateData = 13
    DISPID_SPISaveToMemory = 14
    DISPID_SPIGetText = 15
    DISPID_SPIGetDisplayAttributes = 16


class DISPID_SpeechPhraseElement(IntFlag):
    DISPID_SPEAudioTimeOffset = 1
    DISPID_SPEAudioSizeTime = 2
    DISPID_SPEAudioStreamOffset = 3
    DISPID_SPEAudioSizeBytes = 4
    DISPID_SPERetainedStreamOffset = 5
    DISPID_SPERetainedSizeBytes = 6
    DISPID_SPEDisplayText = 7
    DISPID_SPELexicalForm = 8
    DISPID_SPEPronunciation = 9
    DISPID_SPEDisplayAttributes = 10
    DISPID_SPERequiredConfidence = 11
    DISPID_SPEActualConfidence = 12
    DISPID_SPEEngineConfidence = 13


class DISPID_SpeechPhraseElements(IntFlag):
    DISPID_SPEsCount = 1
    DISPID_SPEsItem = 0
    DISPID_SPEs_NewEnum = -4


class DISPID_SpeechPhraseReplacement(IntFlag):
    DISPID_SPRDisplayAttributes = 1
    DISPID_SPRText = 2
    DISPID_SPRFirstElement = 3
    DISPID_SPRNumberOfElements = 4


class DISPID_SpeechPhraseReplacements(IntFlag):
    DISPID_SPRsCount = 1
    DISPID_SPRsItem = 0
    DISPID_SPRs_NewEnum = -4


class DISPID_SpeechPhraseProperty(IntFlag):
    DISPID_SPPName = 1
    DISPID_SPPId = 2
    DISPID_SPPValue = 3
    DISPID_SPPFirstElement = 4
    DISPID_SPPNumberOfElements = 5
    DISPID_SPPEngineConfidence = 6
    DISPID_SPPConfidence = 7
    DISPID_SPPParent = 8
    DISPID_SPPChildren = 9


class DISPID_SpeechPhraseProperties(IntFlag):
    DISPID_SPPsCount = 1
    DISPID_SPPsItem = 0
    DISPID_SPPs_NewEnum = -4


class DISPID_SpeechPhraseRule(IntFlag):
    DISPID_SPRuleName = 1
    DISPID_SPRuleId = 2
    DISPID_SPRuleFirstElement = 3
    DISPID_SPRuleNumberOfElements = 4
    DISPID_SPRuleParent = 5
    DISPID_SPRuleChildren = 6
    DISPID_SPRuleConfidence = 7
    DISPID_SPRuleEngineConfidence = 8


class DISPID_SpeechPhraseRules(IntFlag):
    DISPID_SPRulesCount = 1
    DISPID_SPRulesItem = 0
    DISPID_SPRules_NewEnum = -4


class DISPID_SpeechLexicon(IntFlag):
    DISPID_SLGenerationId = 1
    DISPID_SLGetWords = 2
    DISPID_SLAddPronunciation = 3
    DISPID_SLAddPronunciationByPhoneIds = 4
    DISPID_SLRemovePronunciation = 5
    DISPID_SLRemovePronunciationByPhoneIds = 6
    DISPID_SLGetPronunciations = 7
    DISPID_SLGetGenerationChange = 8


class DISPID_SpeechLexiconWords(IntFlag):
    DISPID_SLWsCount = 1
    DISPID_SLWsItem = 0
    DISPID_SLWs_NewEnum = -4


class DISPID_SpeechLexiconWord(IntFlag):
    DISPID_SLWLangId = 1
    DISPID_SLWType = 2
    DISPID_SLWWord = 3
    DISPID_SLWPronunciations = 4


class DISPID_SpeechLexiconProns(IntFlag):
    DISPID_SLPsCount = 1
    DISPID_SLPsItem = 0
    DISPID_SLPs_NewEnum = -4


class DISPID_SpeechLexiconPronunciation(IntFlag):
    DISPID_SLPType = 1
    DISPID_SLPLangId = 2
    DISPID_SLPPartOfSpeech = 3
    DISPID_SLPPhoneIds = 4
    DISPID_SLPSymbolic = 5


class DISPID_SpeechPhoneConverter(IntFlag):
    DISPID_SPCLangId = 1
    DISPID_SPCPhoneToId = 2
    DISPID_SPCIdToPhone = 3


class SpeechFormatType(IntFlag):
    SFTInput = 0
    SFTSREngine = 1


class SpeechRecoEvents(IntFlag):
    SREStreamEnd = 1
    SRESoundStart = 2
    SRESoundEnd = 4
    SREPhraseStart = 8
    SRERecognition = 16
    SREHypothesis = 32
    SREBookmark = 64
    SREPropertyNumChange = 128
    SREPropertyStringChange = 256
    SREFalseRecognition = 512
    SREInterference = 1024
    SRERequestUI = 2048
    SREStateChange = 4096
    SREAdaptation = 8192
    SREStreamStart = 16384
    SRERecoOtherContext = 32768
    SREAudioLevel = 65536
    SREPrivate = 262144
    SREAllEvents = 393215


class SpeechRecoContextState(IntFlag):
    SRCS_Disabled = 0
    SRCS_Enabled = 1


class SpeechGrammarState(IntFlag):
    SGSEnabled = 1
    SGSDisabled = 0
    SGSExclusive = 3


class SpeechRuleState(IntFlag):
    SGDSInactive = 0
    SGDSActive = 1
    SGDSActiveWithAutoPause = 3
    SGDSActiveUserDelimited = 4


class SpeechWordPronounceable(IntFlag):
    SWPUnknownWordUnpronounceable = 0
    SWPUnknownWordPronounceable = 1
    SWPKnownWordPronounceable = 2


class SpeechRetainedAudioOptions(IntFlag):
    SRAONone = 0
    SRAORetainAudio = 1


SPAUDIOSTATE = _SPAUDIOSTATE
SPSTREAMFORMATTYPE = SPWAVEFORMATTYPE


__all__ = [
    'Speech_StreamPos_RealTime', 'DISPID_SpeechRecognizerStatus',
    'DISPID_SPRuleParent', 'SpVoice', 'SVP_17', 'SWTAdded',
    'ISpStream', 'DISPID_SRSetPropertyString', 'SAFT16kHz16BitMono',
    'ISpVoice', 'SpeechEngineConfidence', 'DISPID_SPAPhraseInfo',
    'SSSPTRelativeToEnd', 'SVP_6', 'SPSMF_SAPI_PROPERTIES',
    'DISPID_SVAlertBoundary', 'SPINTERFERENCE_NONE', 'SPEI_MAX_TTS',
    'DISPID_SVSkip', 'DISPID_SPCIdToPhone', 'DISPID_SRGDictationLoad',
    'DISPID_SRCEPropertyNumberChange',
    '__MIDL___MIDL_itf_sapi_0000_0020_0002', 'DISPID_SPAsCount',
    'DISPID_SPEAudioStreamOffset', 'DISPID_SRCERequestUI',
    'SREStateChange', 'SP_VISEME_10', 'DISPID_SRGCmdLoadFromObject',
    'SPSHORTCUTPAIR', 'DISPID_SpeechVoiceStatus',
    'DISPID_SWFEBlockAlign', 'DISPID_SWFEBitsPerSample',
    'SPCS_DISABLED', 'SAFT16kHz16BitStereo', 'SpObjectTokenCategory',
    'SRERecoOtherContext', 'DISPID_SpeechPhraseAlternates',
    'SPSEMANTICERRORINFO', 'ISpeechFileStream', 'DISPID_SLPSymbolic',
    'SDA_Consume_Leading_Spaces', 'SECFIgnoreWidth',
    'SPINTERFERENCE_NOSIGNAL', 'DISPID_SpeechAudio',
    'DISPID_SRRAudio', 'DISPID_SPEAudioTimeOffset',
    'DISPID_SPIGetText', 'DISPID_SVResume',
    'DISPID_SOTGetStorageFileName', 'SWTDeleted', 'SPPS_Interjection',
    'eWORDTYPE_ADDED', 'DISPID_SPERequiredConfidence',
    'ISpeechRecognizer', 'SAFT24kHz16BitStereo', 'DISPID_SASState',
    'ISpEventSource', 'DISPID_SVSLastBookmark', 'eLEXTYPE_PRIVATE11',
    'DISPID_SPIGetDisplayAttributes', 'SPEI_VISEME',
    'DISPID_SVGetAudioInputs', 'SVP_2', 'DISPID_SpeechMemoryStream',
    'DISPID_SVVoice', 'SAFTADPCM_8kHzMono', 'ISpNotifySource',
    'ISpeechRecoResultTimes', 'DISPID_SRRPhraseInfo',
    'DISPID_SLWType', 'DISPID_SpeechPhraseRules', 'eLEXTYPE_PRIVATE6',
    'DISPID_SRCState', 'DISPID_SRSetPropertyNumber', '_SPAUDIOSTATE',
    'STSF_FlagCreate', 'SAFTCCITT_ALaw_44kHzStereo',
    'DISPID_SVSVisemeId', 'DISPID_SPRulesCount',
    'DISPID_SOTCGetDataKey', 'SP_VISEME_13', 'SPSSuppressWord',
    'SpeechAudioFormatGUIDWave', 'DISPID_SGRsAdd',
    'DISPID_SAEventHandle', 'SAFT24kHz16BitMono', 'SGRSTTWord',
    'SPEI_SR_RETAINEDAUDIO', 'SAFT12kHz16BitStereo', 'SPAUDIOSTATUS',
    'DISPID_SPIAudioStreamPosition', 'SPWT_LEXICAL',
    'eLEXTYPE_PRIVATE16', 'DISPID_SLGetWords',
    'DISPID_SGRSTs_NewEnum', 'SpeechRecoContextState', 'SLODynamic',
    'SINoise', 'DISPID_SpeechPhraseBuilder',
    'DISPID_SpeechAudioBufferInfo',
    'DISPID_SRAllowAudioInputFormatChangesOnNextSet',
    '_RemotableHandle', 'DISPID_SpeechPhraseProperties',
    'SpeechCategoryRecognizers', 'SPCATEGORYTYPE', 'SVSFParseSapi',
    'SPSHT_Unknown', 'SPSMF_SRGS_SAPIPROPERTIES',
    'SpeechCategoryAudioOut', 'SWPUnknownWordPronounceable',
    'DISPID_SRSNumberOfActiveRules', 'SpeechLoadOption',
    'eLEXTYPE_MORPHOLOGY', 'SpeechGrammarTagDictation', 'SPSUnknown',
    'DISPID_SRCRequestedUIType', 'SPAS_RUN', 'DISPID_SOTDataKey',
    'SVSFPersistXML', 'SP_VISEME_8', 'SVF_Emphasis',
    'DISPID_SRSSupportedLanguages', 'ISpAudio',
    'DISPID_SRCERecognition', 'SINoSignal', 'DISPID_SpeechVoiceEvent',
    'SpInprocRecognizer', 'DISPID_SVGetVoices', 'SpeechAddRemoveWord',
    'DISPID_SRGetFormat', 'DISPID_SRCRecognizer', 'SVP_7',
    'SGDSInactive', 'SPSFunction', 'SPEI_RESERVED1', 'SPBO_AHEAD',
    'SP_VISEME_9', 'DISPID_SAFGuid', 'SGRSTTDictation', 'SP_VISEME_3',
    'SAFTCCITT_uLaw_8kHzMono', 'SDTDisplayText',
    'DISPID_SAFSetWaveFormatEx', 'SRATopLevel', 'SPPHRASERULE',
    'DISPID_SpeechWaveFormatEx', 'DISPID_SGRSTransitions',
    'SREAllEvents', 'DISPID_SPARecoResult', 'ISpNotifyTranslator',
    'SPPARTOFSPEECH', 'DISPID_SLGenerationId', 'SVP_0',
    'SpeechPropertyNormalConfidenceThreshold',
    'DISPID_SRGCmdLoadFromResource', 'SPAUDIOBUFFERINFO',
    'DISPID_SPEEngineConfidence', 'DISPID_SpeechLexiconWords',
    'SREPhraseStart', 'eLEXTYPE_PRIVATE10', 'DISPID_SRCPause',
    'DISPID_SPRsCount', 'DISPID_SPRuleNumberOfElements',
    'DISPID_SFSClose', 'SVSFDefault',
    'ISpeechTextSelectionInformation', 'DISPID_SVEBookmark',
    'SPRST_ACTIVE', 'SpeechAudioProperties',
    'SpeechPropertyComplexResponseSpeed', 'SAFT12kHz16BitMono',
    'SP_VISEME_20', 'eLEXTYPE_RESERVED8', 'SPXMLRESULTOPTIONS',
    'DISPID_SPAs_NewEnum', 'SpPhoneticAlphabetConverter',
    'DISPID_SPCLangId', 'SPGRAMMARSTATE', 'DISPID_SPRFirstElement',
    'SAFTExtendedAudioFormat', 'IEnumString', 'DISPID_SPPsCount',
    'SPAR_Low', 'SpSharedRecoContext', 'DISPID_SAStatus',
    'SAFT44kHz16BitStereo', 'DISPID_SPIElements',
    'SpNotifyTranslator', 'SPPHRASEPROPERTY', 'ISpNotifySink',
    'DISPID_SpeechPhraseRule', 'ISpPhoneticAlphabetConverter',
    'DISPID_SVGetProfiles', 'DISPID_SRAudioInputStream',
    'SPEI_START_SR_STREAM', 'SP_VISEME_0', 'SPPS_Verb',
    'SpeechVoiceCategoryTTSRate', 'ISpRecoContext', 'DISPID_SPRText',
    'DISPID_SPPFirstElement', 'DISPID_SOTMatchesAttributes',
    'SVSFlagsAsync', 'SVF_None', 'SPEVENTSOURCEINFO',
    'SECNormalConfidence', 'DISPID_SPISaveToMemory',
    'ISpRecoContext2', 'eLEXTYPE_PRIVATE7', 'SGRSTTEpsilon',
    'SDKLCurrentConfig', 'SVP_19', 'DISPID_SRGetPropertyString',
    'DISPID_SRCEHypothesis', 'DISPID_SPEs_NewEnum',
    'SpeechAudioFormatGUIDText', 'DISPID_SPPsItem', 'ISpPhrase',
    'SpeechVoiceSkipTypeSentence', 'SpeechPropertyAdaptationOn',
    'DISPID_SpeechObjectTokenCategory', 'ISpRecognizer', 'SPXRO_SML',
    'DISPID_SGRAttributes', 'SRAExport', 'SVP_5', 'STCRemoteServer',
    'DISPID_SLWsCount', 'SPWORDPRONUNCIATION', 'SpeechMicTraining',
    'DISPID_SRCEBookmark', 'SpMMAudioEnum', 'SpeechTokenKeyFiles',
    'DISPID_SRRTimes', 'DISPID_SVSInputSentenceLength',
    'DISPID_SGRsFindRule', 'SRSInactive', 'DISPID_SPRuleConfidence',
    'DISPID_SPIEngineId', 'SVSFIsXML', 'DISPID_SLWPronunciations',
    'SpShortcut', 'DISPID_SRGSetTextSelection',
    'DISPID_SPRuleEngineConfidence', 'SPSHORTCUTPAIRLIST',
    'SAFT8kHz8BitMono', 'DISPID_SMSSetData', 'SVSFIsNotXML',
    'SPPS_RESERVED1', 'DISPID_SRState', 'ISpeechRecoResultDispatch',
    'SSSPTRelativeToStart', 'ISpeechRecognizerStatus',
    'DISPID_SRRecognizer', 'eLEXTYPE_USER_SHORTCUT',
    'SAFTGSM610_44kHzMono', 'SRAONone', 'DISPID_SLWLangId',
    'SpeechDiscardType', 'SpeechCategoryPhoneConverters', 'SVP_11',
    'DISPID_SRGId', 'SPLO_STATIC', 'SpeechRegistryLocalMachineRoot',
    'SPWT_LEXICAL_NO_SPECIAL_CHARS', 'DISPID_SVEventInterests',
    'DISPID_SPIEnginePrivateData',
    'ISpeechGrammarRuleStateTransition', 'ISpeechObjectTokenCategory',
    'SPEI_MIN_SR', 'SPWF_SRENGINE', 'SpUnCompressedLexicon',
    'SPINTERFERENCE_LATENCY_WARNING', 'DISPID_SRCESoundEnd',
    'DISPID_SRCERecognizerStateChange', 'SpeechCategoryRecoProfiles',
    'SPCT_SUB_DICTATION', 'DISPID_SGRName', 'SPCT_SLEEP',
    'DISPID_SVDisplayUI', 'eLEXTYPE_PRIVATE3',
    'DISPID_SVEStreamStart', 'SpWaveFormatEx', 'ISpXMLRecoResult',
    'SPPHRASE', 'SLTUser', 'SPEI_TTS_BOOKMARK', 'SpAudioFormat',
    'DISPID_SPIProperties', 'SpeechRecognitionType', 'SVP_10',
    'SPEI_WORD_BOUNDARY', 'ISpeechGrammarRule', 'SGSExclusive',
    'SAFT11kHz8BitMono', 'DISPID_SPPValue', 'SPFM_CREATE',
    'SDA_No_Trailing_Space', 'SASPause', 'typelib_path',
    'DISPID_SPANumberOfElementsInResult', 'SECFIgnoreCase',
    'DISPIDSPTSI', 'SVEPrivate', 'SPEI_SR_BOOKMARK',
    'ISpeechVoiceStatus', 'SPEI_START_INPUT_STREAM', 'SVSFParseSsml',
    'DISPID_SVSInputWordLength', 'SGDSActiveWithAutoPause',
    'SWPKnownWordPronounceable', 'ISpEventSink',
    'DISPID_SRCRetainedAudio', 'DISPID_SPRulesItem',
    'eLEXTYPE_PRIVATE1', 'DISPIDSPRG', 'SPEI_SOUND_END',
    'SP_VISEME_18', 'DISPID_SABufferInfo', 'SREAdaptation',
    'SPBO_NONE', 'DISPIDSPTSI_ActiveOffset', 'SpeechStreamFileMode',
    'SPEI_TTS_PRIVATE', 'DISPID_SDKDeleteValue',
    'DISPID_SMSADeviceId', 'SINone', 'DISPID_SGRSTWeight',
    'SPCT_DICTATION', 'SVEEndInputStream', 'DISPID_SPPParent',
    'ISpDataKey', 'DISPID_SOTCategory', 'SVPAlert', 'SVPOver',
    'SRSActive', 'SGLexical', 'SPSHT_EMAIL',
    'DISPID_SOTIsUISupported', 'DISPID_SBSWrite',
    'DISPID_SGRInitialState', 'DISPID_SPACommit',
    'SPEI_TTS_AUDIO_LEVEL', 'ISpeechLexiconWord',
    'DISPID_SRCCreateGrammar', 'ISpeechPhraseProperty',
    'SPSNotOverriden', 'SLOStatic', 'SVEVoiceChange',
    'SAFT48kHz16BitStereo', 'SAFT48kHz8BitMono', 'SPSVerb',
    'SAFTADPCM_22kHzStereo', 'SDTPronunciation', 'eLEXTYPE_PRIVATE15',
    'SPPS_Modifier', 'DISPID_SLAddPronunciationByPhoneIds',
    'DISPID_SVSPhonemeId', 'ISpeechPhraseRules', 'tagSPPROPERTYINFO',
    'SVP_18', 'SDTAudio', 'DISPID_SVAudioOutput',
    'DISPID_SGRSTPropertyValue', 'SASClosed', 'SRAInterpreter',
    'SAFTADPCM_44kHzMono', 'STCInprocHandler',
    'SPWP_UNKNOWN_WORD_UNPRONOUNCEABLE', 'eLEXTYPE_RESERVED7',
    'ISpeechMemoryStream', 'SAFTGSM610_11kHzMono', 'ISpeechAudio',
    'SPPHRASEELEMENT', 'DISPID_SRCVoicePurgeEvent', 'SPPS_Noncontent',
    'SPDKL_DefaultLocation', 'SPFILEMODE', 'DISPID_SGRSTsCount',
    'ISpObjectTokenCategory', 'SPEI_FALSE_RECOGNITION',
    'DISPID_SPEsCount', 'SpPhoneConverter',
    'DISPID_SpeechPhraseElements', 'DISPID_SDKDeleteKey',
    'DISPID_SVSyncronousSpeakTimeout', 'SpeechUserTraining',
    'SPLO_DYNAMIC', 'DISPID_SRSAudioStatus',
    'DISPID_SGRSAddSpecialTransition', 'DISPID_SVSpeakCompleteEvent',
    'SPSMF_UPS', 'DISPID_SRCBookmark', 'IInternetSecurityMgrSite',
    'SPBO_PAUSE', 'DISPID_SFSOpen',
    'SpeechPropertyLowConfidenceThreshold', 'SASRun',
    'eLEXTYPE_RESERVED6', 'SVESentenceBoundary',
    'SPWP_KNOWN_WORD_PRONOUNCEABLE', 'DISPID_SOTSetId',
    'DISPID_SOTRemoveStorageFileName', 'SPDKL_CurrentUser',
    'SPGRAMMARWORDTYPE', 'DISPID_SVRate',
    'DISPID_SPPEngineConfidence', 'DISPID_SPEActualConfidence',
    'SPFM_CREATE_ALWAYS', 'DISPID_SGRSAddWordTransition',
    'SGSEnabled', 'SPRECORESULTTIMES', 'DISPID_SLPPhoneIds',
    'DISPID_SPRs_NewEnum', 'eLEXTYPE_APP', 'SPVISEMES',
    'ISpeechXMLRecoResult', 'DISPID_SRCEPhraseStart',
    'ISpGrammarBuilder', 'SASStop', 'DISPID_SLGetGenerationChange',
    'ISpRecognizer3', 'SRTExtendableParse',
    'ISpeechLexiconPronunciation', 'ISpeechLexicon',
    'DISPID_SOTGetDescription', 'SSTTDictation', 'SPGS_ENABLED',
    'DISPID_SRGState', 'DISPID_SGRClear', 'Speech_Max_Pron_Length',
    'SPAUDIOOPTIONS', 'SAFTNonStandardFormat', 'SDKLCurrentUser',
    'DISPID_SpeechPhraseReplacement', 'SITooQuiet',
    'Speech_Default_Weight', 'SVP_8', 'SAFTCCITT_ALaw_22kHzMono',
    'SP_VISEME_15', 'DISPID_SPIRetainedSizeBytes', 'STCInprocServer',
    'SAFT12kHz8BitStereo', 'SAFTCCITT_uLaw_22kHzStereo',
    'DISPID_SPEsItem', 'DISPID_SPPs_NewEnum',
    'DISPID_SRCEEnginePrivate', 'ISpeechPhraseProperties',
    'DISPID_SpeechGrammarRuleState',
    'SPINTERFERENCE_LATENCY_TRUNCATE_END', 'eLEXTYPE_RESERVED10',
    'DISPID_SOTCSetId', 'SECHighConfidence', 'SPWORD',
    'SVSFUnusedFlags', 'DISPID_SGRs_NewEnum', 'DISPID_SpeechLexicon',
    'DISPID_SVEEnginePrivate', 'DISPID_SRGCmdSetRuleIdState',
    'SpeechWordType', 'SPEI_END_INPUT_STREAM', 'IEnumSpObjectTokens',
    'SPEI_END_SR_STREAM', 'SPEI_SR_AUDIO_LEVEL',
    'SpeechVoicePriority', 'SPBOOKMARKOPTIONS', 'DISPID_SOTCDefault',
    'SPEVENTENUM', 'SpeechTokenShellFolder', 'DISPID_SPILanguageId',
    'SpCompressedLexicon', 'DISPID_SAFGetWaveFormatEx',
    'SDTReplacement', 'SPAR_Medium', 'SPEI_PROPERTY_NUM_CHANGE',
    'SPEI_ADAPTATION', 'SPEI_SOUND_START', 'SPRST_NUM_STATES',
    'DISPID_SWFEExtraData', 'DISPID_SpeechPhraseInfo',
    'SPRST_ACTIVE_ALWAYS', 'SPTEXTSELECTIONINFO', 'SpeechRuleState',
    'ISpeechAudioFormat', 'DISPID_SLPsItem', 'SVP_4',
    'DISPID_SWFESamplesPerSec', 'DISPID_SVStatus',
    'SAFT11kHz8BitStereo', 'DISPID_SBSFormat', 'SPEI_PHRASE_START',
    'SPEI_RESERVED5', 'SPWP_UNKNOWN_WORD_PRONOUNCEABLE',
    'DISPID_SRSCurrentStreamNumber', 'SPAO_RETAIN_AUDIO',
    'SPPS_RESERVED4', 'DISPID_SDKCreateKey',
    'SAFTCCITT_ALaw_11kHzStereo', 'ISpResourceManager',
    'DISPIDSPTSI_ActiveLength', 'SPSNoun',
    'SpeechPropertyResourceUsage', 'ISpObjectToken', 'SPEI_RESERVED6',
    'DISPID_SpeechGrammarRuleStateTransitions',
    '__MIDL___MIDL_itf_sapi_0000_0020_0001', 'SRTEmulated',
    'SVSFParseMask', 'SRERecognition', 'SPDATAKEYLOCATION',
    'DISPID_SRIsShared', 'DISPID_SPEAudioSizeBytes',
    'ISpeechPhraseReplacement', 'SRESoundStart',
    'SAFTADPCM_11kHzStereo', 'DISPID_SRCAudioInInterferenceStatus',
    'SpeechTokenIdUserLexicon', 'DISPID_SASFreeBufferSpace',
    'DISPID_SpeechXMLRecoResult', 'ISpeechPhraseInfoBuilder',
    'SAFT11kHz16BitMono', 'SpeechWordPronounceable',
    'DISPID_SPPConfidence', 'ISpeechWaveFormatEx',
    'SpInProcRecoContext', 'DISPID_SADefaultFormat', 'SLTApp',
    'SFTInput', 'ISpRecoGrammar2', 'SPSHORTCUTTYPE',
    'ISpRecoCategory', 'ISpeechAudioBufferInfo',
    'SSSPTRelativeToCurrentPosition', 'SREAudioLevel',
    'SpStreamFormatConverter', 'SP_VISEME_14', 'SVP_15',
    'DISPID_SRStatus', 'DISPID_SpeechBaseStream', 'SVEWordBoundary',
    'DISPID_SGRAddState', 'DISPID_SRRRecoContext',
    'DISPID_SpeechPhraseElement', 'SPINTERFERENCE_TOOQUIET',
    'SpeechRecoEvents', 'SAFT22kHz16BitStereo', 'SAFT44kHz16BitMono',
    'SPCS_ENABLED', 'DISPID_SGRsItem',
    'DISPID_SpeechLexiconPronunciation',
    'SpeechRecoProfileProperties',
    'SpeechGrammarTagUnlimitedDictation', 'SAFT8kHz16BitStereo',
    'DISPID_SLWsItem', 'SECLowConfidence', 'ISpShortcut',
    'SpeechDisplayAttributes', 'SPGS_DISABLED', 'ISpeechRecoResult',
    'SP_VISEME_17', 'ISpPhoneticAlphabetSelection', 'ISpeechDataKey',
    'SRCS_Disabled', 'SP_VISEME_2', 'DISPID_SCSBaseStream',
    'DISPID_SDKGetStringValue', 'SpFileStream', 'SAFT22kHz8BitStereo',
    'STSF_CommonAppData', 'ISpeechGrammarRules', 'SPPS_LMA',
    'DISPID_SRRAudioFormat', 'DISPID_SRCRetainedAudioFormat',
    'SPINTERFERENCE_NOISE', 'DISPID_SWFEFormatTag', 'SPAUDIOSTATE',
    'SpeechGrammarRuleStateTransitionType', 'SPPS_RESERVED2',
    'DISPID_SDKEnumKeys', 'SPAR_Unknown', 'DISPID_SPRuleName',
    'DISPID_SVEWord', 'DISPID_SRAudioInput', 'DISPID_SRRSpeakAudio',
    'SRSActiveAlways', 'DISPID_SVAudioOutputStream',
    'DISPID_SVEStreamEnd', 'SAFT44kHz8BitStereo',
    'DISPID_SPAStartElementInResult', 'SPPS_RESERVED3',
    'SAFT22kHz8BitMono', 'SPSMF_SRGS_SEMANTICINTERPRETATION_W3C',
    'SPLOADOPTIONS', 'DISPID_SGRAddResource', 'DISPID_SRRTLength',
    'SPEI_MAX_SR', 'DISPID_SREmulateRecognition', 'SAFTText',
    'SREBookmark', 'eLEXTYPE_PRIVATE17', 'eLEXTYPE_PRIVATE9',
    'eWORDTYPE_DELETED', 'ISpeechVoice', 'DISPID_SVSRunningState',
    'DISPID_SRGDictationSetState', 'DISPID_SpeechLexiconWord',
    'SPPS_Function', 'SpeechRunState', 'SAFTCCITT_ALaw_11kHzMono',
    'SpeechRuleAttributes', 'SREStreamStart', 'SRSEDone',
    'SpObjectToken', 'ISpeechPhoneConverter', 'DISPID_SGRSTRule',
    'DISPID_SRIsUISupported', 'SPRECOSTATE', 'SSFMCreateForWrite',
    'SVSFNLPSpeakPunc', 'DISPID_SMSGetData', 'DISPID_SPELexicalForm',
    'SPPROPERTYINFO', 'SECFIgnoreKanaType', 'SFTSREngine',
    'SPVOICESTATUS', 'SVP_3', 'SpeechRegistryUserRoot',
    'SpeechPropertyResponseSpeed', 'DISPID_SRGCmdSetRuleState',
    'SpeechGrammarWordType', 'DISPID_SRCVoice', 'SPCT_SUB_COMMAND',
    'eLEXTYPE_LETTERTOSOUND', 'DISPID_SOTs_NewEnum',
    'DISPID_SPRuleFirstElement', 'SDKLDefaultLocation',
    'DISPID_SLWs_NewEnum', 'SpeechAllElements',
    'DISPID_SpeechPhoneConverter', 'SDTProperty',
    'DISPID_SVSLastStreamNumberQueued', 'SP_VISEME_5',
    'DISPID_SRGIsPronounceable', 'SAFT48kHz8BitStereo',
    'DISPID_SVSpeak', 'eLEXTYPE_PRIVATE19', 'DISPID_SOTCId',
    'SAFTDefault', 'SRTSMLTimeout', 'DISPID_SRSCurrentStreamPosition',
    'SRCS_Enabled', 'eLEXTYPE_RESERVED4',
    'DISPID_SRCEFalseRecognition', 'DISPID_SRRGetXMLErrorInfo',
    'ISpeechPhraseAlternate', 'eLEXTYPE_PRIVATE8', 'DISPID_SVVolume',
    'DISPID_SOTRemove', 'DISPID_SASNonBlockingIO',
    'ISpeechPhraseAlternates', 'SPADAPTATIONRELEVANCE', 'SVP_13',
    'SpTextSelectionInformation', 'ISpeechPhraseRule',
    'SAFTCCITT_uLaw_11kHzStereo', 'SPWORDPRONOUNCEABLE', 'SREPrivate',
    'DISPID_SPAsItem', 'DISPID_SpeechGrammarRule', 'DISPID_SRGCommit',
    'DISPID_SRCEEndStream', 'ISpRecognizer2', 'SPVPRI_NORMAL',
    'ISpStreamFormat', 'DISPID_SOTCreateInstance',
    'DISPID_SOTDisplayUI', '_ISpeechVoiceEvents', 'LONG_PTR',
    'DISPID_SLRemovePronunciation', 'SPSHT_OTHER',
    'DISPID_SVIsUISupported', 'ISpPhoneConverter',
    'DISPID_SPRDisplayAttributes', 'SpPhraseInfoBuilder',
    'DISPID_SRRSaveToMemory', 'ISpeechLexiconWords',
    'DISPID_SDKGetlongValue', 'SPINTERFERENCE_TOOFAST',
    'DISPID_SOTsCount', 'SAFTCCITT_uLaw_22kHzMono',
    'SpeechAudioState', 'SPFM_OPEN_READWRITE',
    'SAFTTrueSpeech_8kHz1BitMono', 'DISPID_SRGReset',
    'DISPID_SBSSeek', 'SPCONTEXTSTATE', 'DISPID_SOTCEnumerateTokens',
    'SVSFVoiceMask', 'SAFT24kHz8BitMono', 'SpeechVoiceEvents',
    'SAFT12kHz8BitMono', 'SITooSlow', 'SPVPRIORITY',
    'DISPID_SpeechAudioStatus', 'SAFT8kHz8BitStereo',
    'DISPID_SpeechRecoContext', 'DISPID_SVSCurrentStreamNumber',
    'DISPID_SRGCmdLoadFromFile', 'ISpeechPhraseReplacements',
    'eLEXTYPE_PRIVATE20', 'DISPID_SLRemovePronunciationByPhoneIds',
    'SPRST_INACTIVE', 'eLEXTYPE_PRIVATE4', 'SPEI_RESERVED2',
    'DISPID_SVEVoiceChange', 'SP_VISEME_6', 'ISpPhraseAlt',
    'SPINTERFERENCE_TOOSLOW', 'SPPS_SuppressWord',
    'SAFTCCITT_uLaw_11kHzMono', 'SVP_12', 'ISpeechMMSysAudio',
    'SP_VISEME_1', 'SAFT32kHz16BitMono', 'SP_VISEME_11',
    'DISPID_SASCurrentDevicePosition', 'DISPID_SpeechVoice',
    'SECFEmulateResult', 'ISpeechPhraseInfo', 'SAFT48kHz16BitMono',
    'DISPID_SRAllowVoiceFormatMatchingOnNextSet',
    'DISPID_SPRules_NewEnum', 'DISPID_SPEPronunciation',
    'DISPID_SPERetainedStreamOffset', 'SPEI_RESERVED3',
    'SAFTCCITT_ALaw_8kHzMono', 'DISPID_SGRsCommitAndSave',
    'DISPID_SGRsDynamic', 'SPWF_INPUT', 'SGRSTTTextBuffer',
    'ISpeechPhraseElement', 'SPSLMA', 'DISPID_SDKGetBinaryValue',
    'ISpMMSysAudio', 'DISPID_SABufferNotifySize',
    'DISPID_SRGetPropertyNumber', 'SAFT8kHz16BitMono',
    'SREPropertyStringChange', 'SVPNormal', 'SPDKL_LocalMachine',
    'SAFT24kHz8BitStereo', 'ISpeechAudioStatus', 'DISPID_SPPId',
    'SpeechCategoryAppLexicons', 'DISPID_SVSInputWordPosition',
    'DISPID_SpeechRecoResult2', 'DISPID_SPIReplacements',
    'SPRS_INACTIVE', 'ISpeechResourceLoader',
    'ISpeechGrammarRuleState', 'ISpeechObjectToken',
    'SPEI_REQUEST_UI', 'DISPID_SVPriority', 'SPDKL_CurrentConfig',
    'SVP_21', 'DISPID_SpeechMMSysAudio', 'SPEI_SR_PRIVATE',
    'SDKLLocalMachine', 'SpeechCategoryAudioIn', 'DISPID_SRDisplayUI',
    'SRADynamic', 'SDTLexicalForm', 'DISPID_SDKEnumValues',
    'SGRSTTRule', 'SP_VISEME_21', 'SPEI_PHONEME', 'DISPID_SPIRule',
    'DISPID_SpeechLexiconProns', 'DISPID_SPIAudioSizeBytes',
    'SPWORDTYPE', 'IStream', 'eLEXTYPE_PRIVATE12',
    'tagSPTEXTSELECTIONINFO', 'SP_VISEME_16', 'SpResourceManager',
    'SPEI_MIN_TTS', 'SpeechLexiconType', 'DISPID_SRCreateRecoContext',
    'DISPID_SVEAudioLevel', 'SVEPhoneme', 'SPEI_INTERFERENCE',
    'SpeechTokenKeyUI', 'SP_VISEME_19',
    'DISPID_SRCEPropertyStringChange', 'SVSFParseAutodetect',
    'SpeechCategoryVoices', 'DISPID_SRCERecognitionForOtherContext',
    'DISPID_SRGCmdLoadFromMemory', 'DISPID_SGRId', 'DISPID_SGRSTType',
    'SpeechTokenValueCLSID', 'SREInterference',
    'SpeechDataKeyLocation', 'SGDisplay', 'SRTReSent', 'SPAS_PAUSE',
    'DISPID_SRGetRecognizers', 'SPRULE', 'DISPID_SVSLastBookmarkId',
    'SBOPause', 'SAFTGSM610_22kHzMono', 'SPEI_HYPOTHESIS',
    'DISPID_SRRTOffsetFromStart', 'DISPID_SLWWord', 'SpLexicon',
    'ISpeechBaseStream', 'SAFTCCITT_ALaw_44kHzMono', 'SDTAll',
    'SPINTERFERENCE_TOOLOUD', 'SDTRule', 'SPSERIALIZEDPHRASE',
    'SRERequestUI', 'SPLEXICONTYPE', 'SREFalseRecognition',
    'DISPID_SPEDisplayAttributes', 'SGSDisabled', 'SPWT_DISPLAY',
    'SRAImport', 'SPPS_Noun', 'ISpeechCustomStream', 'eLEXTYPE_USER',
    'DISPID_SPEAudioSizeTime', 'DISPID_SLPLangId', 'SSTTTextBuffer',
    'eLEXTYPE_PRIVATE14', 'SPGS_EXCLUSIVE', 'SPWT_PRONUNCIATION',
    'eLEXTYPE_PRIVATE2', 'DISPID_SMSAMMHandle', 'SpCustomStream',
    'SPAR_High', 'SAFT44kHz8BitMono', 'SREStreamEnd',
    'DISPID_SpeechRecognizer', 'DISPID_SVESentenceBoundary',
    'SGRSTTWildcard', 'SPRECOGNIZERSTATUS', 'eLEXTYPE_PRIVATE13',
    'DISPID_SPRuleChildren', 'SpeechSpecialTransitionType',
    'SP_VISEME_12', 'SpStream', 'SAFT32kHz16BitStereo',
    'SPEI_VOICE_CHANGE', 'SPEI_RECO_STATE_CHANGE',
    'ISpeechRecoContext', 'SAFTADPCM_8kHzStereo',
    'SPWORDPRONUNCIATIONLIST', 'SVP_9', 'SPVPRI_OVER',
    'DISPID_SRRAlternates', 'SAFT32kHz8BitStereo',
    'SAFT16kHz8BitStereo', 'ISpeechRecoResult2', 'SpeechInterference',
    'DISPID_SRCEAudioLevel', 'DISPIDSPTSI_SelectionOffset',
    'DISPID_SPIGrammarId', 'DISPID_SPRsItem', 'DISPID_SDKOpenKey',
    'SPBO_TIME_UNITS', 'UINT_PTR', 'DISPID_SVPause',
    'STSF_LocalAppData', 'SPFM_OPEN_READONLY', 'SpeechPartOfSpeech',
    'DISPID_SAFType', 'SRTAutopause', 'DISPID_SPPChildren',
    'SVEViseme', 'DISPID_SRGSetWordSequenceData', 'SPSInterjection',
    'SDTAlternates', 'SpeechEmulationCompareFlags',
    'SPWAVEFORMATTYPE', 'STCLocalServer', 'eLEXTYPE_VENDORLEXICON',
    'DISPID_SABIMinNotification', 'DISPID_SGRSAddRuleTransition',
    'SITooFast', 'SpMMAudioOut', 'SPAS_STOP', 'SECFDefault',
    'WAVEFORMATEX', 'SAFT11kHz16BitStereo', 'SAFTADPCM_11kHzMono',
    'eLEXTYPE_PRIVATE5', 'ISpLexicon', 'DISPID_SPRuleId',
    'DISPID_SVSpeakStream', 'DISPID_SVEViseme', 'SRARoot', 'SVP_14',
    'SVEStartInputStream', 'DISPID_SDKSetStringValue',
    'DISPID_SpeechRecoResult', 'SGPronounciation',
    'SWPUnknownWordUnpronounceable', 'DISPID_SRProfile',
    'DISPID_SRCEInterference', 'SVEAudioLevel', 'SpeechTokenContext',
    'DISPID_SRGCmdLoadFromProprietaryGrammar',
    'DISPID_SRCCreateResultFromMemory', 'SPAO_NONE',
    'SpeechGrammarTagWildcard', 'ISpProperties', 'SpeechGrammarState',
    'DISPID_SpeechDataKey', 'tagSTATSTG', 'SPRS_ACTIVE',
    'SpeechVisemeFeature', 'SVSFPurgeBeforeSpeak', 'SPPS_Unknown',
    'SSFMOpenReadWrite', 'SpeechVisemeType',
    'ISpeechGrammarRuleStateTransitions', 'SAFTNoAssignedFormat',
    'SPINTERFERENCE_LATENCY_TRUNCATE_BEGIN', 'SAFT16kHz8BitMono',
    'DISPID_SpeechPhraseProperty', 'STCAll',
    'DISPID_SRCSetAdaptationData', 'SPEI_RECOGNITION',
    'SAFTCCITT_ALaw_22kHzStereo', 'SPSERIALIZEDRESULT',
    'DISPID_SRCEStartStream', 'SPEI_UNDEFINED',
    'DISPID_SRCEAdaptation', 'SVP_20', 'SPSTREAMFORMATTYPE',
    'SVEAllEvents', 'SPSHT_NotOverriden', 'DISPID_SVGetAudioOutputs',
    'DISPID_SRCCmdMaxAlternates', 'ISpeechPhraseElements',
    '_ISpeechRecoContextEvents', 'SAFTCCITT_uLaw_44kHzStereo',
    'SpeechRetainedAudioOptions', 'DISPID_SBSRead',
    'DISPID_SRRGetXMLResult', 'SPEI_ACTIVE_CATEGORY_CHANGED',
    'SPEI_RECO_OTHER_CONTEXT', 'DISPID_SRGRules',
    'DISPID_SPPBRestorePhraseFromMemory', 'SpMMAudioIn',
    'SPBINARYGRAMMAR', 'DISPID_SPEDisplayText', 'SpeechAudioVolume',
    'DISPID_SPIStartTime', 'DISPID_SGRSTPropertyId',
    'SPRECOCONTEXTSTATUS', 'SPPHRASEREPLACEMENT',
    'DISPID_SRGRecoContext', 'SPSMF_SRGS_SEMANTICINTERPRETATION_MS',
    'SpeechPropertyHighConfidenceThreshold', 'SP_VISEME_7',
    'ISpRecoGrammar', 'SREHypothesis', 'SECFNoSpecialChars',
    'SAFT32kHz8BitMono', 'DISPID_SLAddPronunciation',
    'SPRST_INACTIVE_WITH_PURGE', 'DISPID_SRSClsidEngine',
    'DISPID_SPPNumberOfElements', 'SPFM_NUM_MODES', 'SPWORDLIST',
    'SPXRO_Alternates_SML', 'SSTTWildcard',
    'DISPID_SRGDictationUnload', 'DISPID_SRRDiscardResultInfo',
    'DISPID_SRCESoundStart', 'SRSInactiveWithPurge',
    'DISPID_SpeechGrammarRuleStateTransition',
    'DISPID_SpeechPhraseAlternate', 'SDA_One_Trailing_Space',
    'DISPID_SpeechCustomStream', 'SGDSActive',
    'DISPID_SLGetPronunciations', 'SpeechEngineProperties',
    'DISPID_SASetState', 'SAFTCCITT_uLaw_44kHzMono', 'SPSModifier',
    'SpMemoryStream', 'SPCT_COMMAND', 'DISPID_SRCEventInterests',
    'DISPID_SRRTTickCount', 'DISPID_SPPName', 'SRESoundEnd',
    'Speech_Max_Word_Length', 'DISPID_SpeechObjectTokens',
    'SPEI_PROPERTY_STRING_CHANGE', 'DISPID_SpeechGrammarRules',
    'SpeechTokenKeyAttributes', 'SPPS_NotOverriden',
    'SpeechDictationTopicSpelling', 'DISPID_SGRSTNextState',
    'DISPID_SLPPartOfSpeech', 'SAFT22kHz16BitMono',
    'DISPID_SVSInputSentencePosition', 'eLEXTYPE_RESERVED9',
    'DISPID_SWFEAvgBytesPerSec', 'DISPID_SGRsCommit', 'SITooLoud',
    'SPRS_ACTIVE_USER_DELIMITED', 'SpSharedRecognizer',
    'DISPID_SRRTStreamTime', 'DISPID_SVWaitUntilDone',
    'DISPID_SVSLastResult', 'DISPID_SPCPhoneToId', 'DISPID_SOTsItem',
    'SpeechFormatType', 'DISPID_SDKSetBinaryValue',
    'eLEXTYPE_PRIVATE18', 'DISPID_SOTId',
    'DISPID_SASCurrentSeekPosition', 'SAFTADPCM_44kHzStereo',
    'SVSFIsFilename', 'IInternetSecurityManager',
    'DISPID_SGRSTPropertyName', 'DISPID_SVEPhoneme',
    'DISPID_SpeechObjectToken', 'SpNullPhoneConverter',
    'SpeechRecognizerState', 'SREPropertyNumChange',
    'ISpeechLexiconPronunciations', 'Library', 'DISPID_SWFEChannels',
    'DISPID_SAVolume', 'ISpRecoResult', 'SVP_1', 'DISPID_SGRsCount',
    'SPINTERFERENCE', 'SSFMOpenForRead', 'ISpStreamFormatConverter',
    'SPAS_CLOSED', 'SpeechBookmarkOptions', 'DISPID_SGRSRule',
    'DISPID_SGRSTText', 'SGLexicalNoSpecialChars', 'DISPID_SRCResume',
    'SAFTADPCM_22kHzMono', 'SVEBookmark', 'DISPID_SLPType',
    'DISPID_SPERetainedSizeBytes', 'ISpSerializeState',
    'SPSEMANTICFORMAT', 'STSF_AppData', 'DISPID_SABIBufferSize',
    'DISPID_SABIEventBias', 'SPEVENT', 'DISPID_SpeechRecoResultTimes',
    'SVP_16', '__MIDL_IWinTypes_0009', 'ISpeechObjectTokens',
    'SRAORetainAudio', 'SGDSActiveUserDelimited', 'SPVPRI_ALERT',
    'SBONone', 'SPRS_ACTIVE_WITH_AUTO_PAUSE', 'SVSFNLPMask',
    'DISPID_SDKSetLongValue', 'SVF_Stressed',
    'SDA_Two_Trailing_Spaces', 'ISpObjectWithToken',
    'DISPID_SVAllowAudioOuputFormatChangesOnNextSet',
    'DISPID_SRRSetTextFeedback', 'SpeechVoiceSpeakFlags',
    'DISPIDSPTSI_SelectionLength', 'SRADefaultToActive',
    'SPEI_SENTENCE_BOUNDARY', 'DISPID_SpeechRecoContextEvents',
    'DISPID_SOTGetAttribute', 'SpeechAudioFormatType', 'SRTStandard',
    'DISPID_SPIAudioSizeTime', 'DISPID_SLPs_NewEnum',
    'DISPID_SpeechPhraseReplacements', 'Speech_StreamPos_Asap',
    'SSFMCreate', 'DISPID_SLPsCount', 'ISpeechRecoGrammar',
    'SRSEIsSpeaking', 'SAFTCCITT_ALaw_8kHzStereo',
    'DISPID_SGRSTsItem', 'SAFTCCITT_uLaw_8kHzStereo',
    'DISPID_SPRNumberOfElements', 'SP_VISEME_4',
    'DISPID_SpeechAudioFormat', 'DISPID_SpeechFileStream',
    'SPRULESTATE', 'DISPID_SMSALineId',
    'SpeechStreamSeekPositionType', 'SAFTGSM610_8kHzMono'
]

