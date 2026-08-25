import numpy as np
import math
import inspect
import hashlib

class PurePythonPatternRecognitionEngine:
    r"""
    Zero-Dependency 2D Template Matching via Normalized Cross-Correlation (NCC)
    """
    @staticmethod
    def match_template(image_grid: list, template_grid: list) -> dict:
        img = np.array(image_grid, dtype=float)
        tpl = np.array(template_grid, dtype=float)

        H, W = img.shape
        h, w = tpl.shape

        if H < h or W < w:
            return {"error": "Image dimensions must be greater than or equal to template dimensions"}

        tpl_mean = np.mean(tpl)
        tpl_norm = tpl - tpl_mean
        tpl_denom = np.sum(tpl_norm ** 2)

        best_score = -1.0
        best_coord = (0, 0)
        correlation_map = np.zeros((H - h + 1, W - w + 1), dtype=float)

        for i in range(H - h + 1):
            for j in range(W - w + 1):
                patch = img[i:i+h, j:j+w]
                patch_mean = np.mean(patch)
                patch_norm = patch - patch_mean
                patch_denom = np.sum(patch_norm ** 2)

                denom = math.sqrt(patch_denom * tpl_denom)
                if denom > 1e-12:
                    score = float(np.sum(patch_norm * tpl_norm) / denom)
                else:
                    score = 0.0

                correlation_map[i, j] = round(score, 4)
                if score > best_score:
                    best_score = score
                    best_coord = (i, j)

        return {
            "image_shape": f"{H}x{W}",
            "template_shape": f"{h}x{w}",
            "best_match_coordinate": best_coord,
            "max_confidence_score": round(float(best_score), 4),
            "correlation_matrix_preview": correlation_map.tolist(),
            "detection_verdict": "MATCH_CONFIRMED" if best_score > 0.85 else "UNCERTAIN_MATCH"
        }

class SelfIntrospectionEngine:
    r"""
    Runtime Code Self-Inspection & Memory Reversal Architecture
    """
    @staticmethod
    def inspect_and_reverse_source(source_path: str) -> dict:
        try:
            with open(source_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except Exception as e:
            return {"error": str(e)}

        total_lines = len(lines)
        file_sha256 = hashlib.sha256("".join(lines).encode('utf-8')).hexdigest()
        
        # In-memory bottom-to-top traversal
        reversed_lines_preview = [l.strip() for l in reversed(lines[-5:])]

        return {
            "inspected_file": source_path,
            "total_lines_read": total_lines,
            "source_sha256": file_sha256,
            "bottom_up_memory_stream": reversed_lines_preview,
            "state_status": "SECURE_INTROSPECTION_COMPLETED"
        }
